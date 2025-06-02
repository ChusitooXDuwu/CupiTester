import ast
import argparse
import re
from typing import List, Dict, Tuple, Any
from syntax import check_syntax
from context import extraer_funciones_a_calificar

FORBIDDEN_MAP: Dict[str, Any] = {
    'if': ast.If,
    'for': ast.For,
    'while': ast.While,
    'import': (ast.Import, ast.ImportFrom),
    'with': ast.With,
    'try': ast.Try,
    'lambda': ast.Lambda,
    'ListComp': ast.ListComp,
    'SetComp': ast.SetComp,
    'DictComp': ast.DictComp,
    'comprehension': ast.comprehension,
    'GeneratorExp': ast.GeneratorExp,
    'Dict': ast.Dict,
    'List': ast.List,
    'Set': ast.Set,
    'Tuple': ast.Tuple,
    'Dict': ast.Dict,
    'List': ast.List,
    'Set': ast.Set,
}

LEVEL_FORBIDDEN: Dict[int, List[str]] = {
    1: ['if', 'for', 'while'],
    2: ['for', 'while'],
    3: ['while'],
    4: ['for'],
}

def check_forbidden_syntax(file_path: str, syntax_results: Dict[str, Tuple[bool, str]], level: int) -> Dict[str, Tuple[bool, str]]:
    """
    Verifica la sintaxis prohibida en el código del estudiante.

    Args:
        file_path (str): La ruta del archivo de código Python del estudiante.
        syntax_results (Dict[str, Tuple[bool, str]]): Diccionario de resultados de sintaxis.
        level (int): Nivel de sintaxis a verificar.
    
    Returns:
        Dict[str, Tuple[bool, str]]: Diccionario de resultados de sintaxis prohibida.
    """
    results: Dict[str, Tuple[bool, str]] = {}
    valid_funcs = [f for f, (ok, _) in syntax_results.items() if ok]
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    forbidden_keys = LEVEL_FORBIDDEN.get(level, [])

    for func in valid_funcs:
        def_pattern = re.compile(rf'^\s*def\s+{re.escape(func)}\s*\(.*\)\s*->.*:\s*$')
        block: List[str] = []
        start_indent = None
        in_block = False
        for line in lines:
            if not in_block:
                if def_pattern.match(line):
                    in_block = True
                    start_indent = len(line) - len(line.lstrip())
                    block.append(line)
            else:
                indent = len(line) - len(line.lstrip())
                if not line.strip() or indent > start_indent:
                    block.append(line)
                else:
                    break
                
        found: List[str] = []
        if block:
            snippet = ''.join(block)
            try:
                tree = ast.parse(snippet)
                for key in forbidden_keys:
                    node_type = FORBIDDEN_MAP.get(key)
                    if node_type and any(isinstance(n, node_type) for n in ast.walk(tree)):
                        found.append(key)
            except SyntaxError:
                results[func] = (False, 'parse_error')
                continue
        else:
            results[func] = (False, 'not_found')
            continue

        if found:
            results[func] = (False, f"prohibidas: {found}")
        else:
            results[func] = (True, '')

    for func, (ok, msg) in syntax_results.items():
        if not ok:
            results[func] = (False, f"syntax_error: {msg}")

    return results

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Chequea sintaxis prohibida según nivel en funciones con TODO')
    parser.add_argument('solution_path', help='Ruta al archivo Python')
    parser.add_argument('student_path', help='Ruta del archivo del estudiante')
    parser.add_argument('level', type=int, choices=range(1,5),help='Nivel de restricción (1-4)')
    args = parser.parse_args()

    funcs = extraer_funciones_a_calificar(args.solution_path)
    syntax_results = check_syntax(args.student_path, funcs)
    results = check_forbidden_syntax(args.student_path, syntax_results, args.level)

    for func, (ok, msg) in results.items():
        if ok:
            print(f"{func}: OK")
        else:
            print(f"{func}: ERROR -> {msg}")