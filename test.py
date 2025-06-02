import importlib.util
import sys
import doctest
from typing import Dict, Tuple, List
import argparse
import json
from context import extraer_funciones_a_calificar
from syntax import check_syntax
from forbidden import check_forbidden_syntax


def load_module_from_path(name: str, path: str):
    """
    Carga un módulo dado su path de archivo sin agregarlo al sys.path.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def extract_doctest_docstrings(solution_path: str,func_names: List[str]) -> Dict[str, str]:
    """
    Carga el módulo de solución y extrae las docstrings (con ejemplos doctest)
    de cada función especificada.

    Args:
        solution_path: Ruta al archivo con las funciones de solución.
        func_names: Lista de nombres de funciones a extraer.

    Returns:
        Diccionario {func_name: docstring} donde docstring puede ser None.
    """
    sol_mod = load_module_from_path('solution', solution_path)
    doctest_map: Dict[str, str] = {}
    for func in func_names:
        obj = getattr(sol_mod, func, None)
        if obj is None:
            doctest_map[func] = None
        else:
            doctest_map[func] = obj.__doc__
    return doctest_map


def inject_doctests(student_path: str,doctest_map: Dict[str, str]) -> object:
    """
    Carga el módulo del estudiante e inyecta las docstrings extraídas en sus funciones.

    Args:
        student_path: Ruta al archivo del estudiante.
        doctest_map: Diccionario {func_name: docstring}.

    Returns:
        El módulo del estudiante con docstrings modificadas.
    """
    stu_mod = load_module_from_path('student', student_path)
    for func, doc in doctest_map.items():
        if not hasattr(stu_mod, func):
            continue
        
        setattr(stu_mod, func, stu_mod.__dict__[func])
        if doc:
            stu_mod.__dict__[func].__doc__ = doc
    return stu_mod


def run_injected_doctests(student_module: object, func_names: List[str]) -> Dict[str, Tuple[bool, List[Dict[str, str]]]]:
    """
    Ejecuta los doctests inyectados en el módulo del estudiante solo para las funciones dadas.

    Args:
        student_module: Módulo del estudiante (con docstrings ya inyectadas).
        func_names: Lista de nombres de funciones a testear.

    Returns:
        Diccionario {func_name: (ok, failures)}.
    """
    finder = doctest.DocTestFinder()
    failures_map: Dict[str, List[Dict[str, str]]] = {fn: [] for fn in func_names}

    class CollectorRunner(doctest.DocTestRunner):
        def __init__(self):
            super().__init__()
            self.collected: List[tuple] = []
        def report_failure(self, out, test, example, got):
            self.collected.append((test, example, got))
            super().report_failure(out, test, example, got)

    runner = CollectorRunner()

    all_tests = finder.find(student_module)
    for test in all_tests:
        func = test.name.split('.')[-1]
        if func not in func_names:
            continue
        runner.run(test)

    for test, example, got in runner.collected:
        func = test.name.split('.')[-1]
        failures_map.setdefault(func, []).append({
            'source': example.source.strip(),
            'want': example.want.strip(),
            'got': got.strip(),
        })

    results: Dict[str, Tuple[bool, List[Dict[str, str]]]] = {}
    for func in func_names:
        fails = failures_map.get(func, [])
        results[func] = (len(fails) == 0, fails)
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ejecuta los doctests inyectados en funciones del estudiante'
    )
    parser.add_argument('solution_path', help='Ruta al archivo con la solución')
    parser.add_argument('student_path', help='Ruta al archivo del estudiante')
    parser.add_argument('level', type=int, choices=range(1,5),help='Nivel de restricciones (1-4)')
    args = parser.parse_args()

    funcs = extraer_funciones_a_calificar(args.student_path)
    syntax_results = check_syntax(args.student_path, funcs)
    forbidden_results = check_forbidden_syntax(args.student_path, syntax_results, args.level)
    
    ok_funcs = [f for f, (ok, _) in forbidden_results.items() if ok]

    doctest_map = extract_doctest_docstrings(args.solution_path, ok_funcs)
    stu_mod = inject_doctests(args.student_path, doctest_map)
    doctest_results = run_injected_doctests(stu_mod, ok_funcs)

    print(json.dumps(doctest_results, indent=2, ensure_ascii=False))
