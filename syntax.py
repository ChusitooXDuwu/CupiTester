import re
from typing import List, Dict, Tuple
from context import extraer_funciones_a_calificar
import argparse

def check_syntax(file_path: str, func_names: List[str]) -> Dict[str, Tuple[bool, str]]:
    """ 
    Verifica si las funciones a calificar tienen sintaxis correcta.
    
    Args:
        file_path (str): La ruta del archivo de código Python del estudiante.
        func_names (List[str]): Las funciones a calificar.
        
    Returns:
        Dict[str, Tuple[bool, str]]: Un diccionario con las funciones a calificar y si tienen sintaxis correcta.
    """
    results: Dict[str, Tuple[bool, str]] = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for func in func_names:
        def_pattern = re.compile(rf'^\s*def\s+{re.escape(func)}\s*\(.*\)\s*->.*:\s*$')
        block: List[str] = []
        start_indent: int = 0
        found = False
        for line in lines:
            if not found:
                if def_pattern.match(line):
                    found = True
                    start_indent = len(line) - len(line.lstrip())
                    block.append(line)
            else:
                indent = len(line) - len(line.lstrip())
                if not line.strip() or indent > start_indent:
                    block.append(line)
                else:
                    break
        if not found:
            results[func] = (False, f"Definición de función '{func}' no encontrada")
            continue
        snippet = ''.join(block)
        try:
            compile(snippet, file_path, 'exec')
            results[func] = (True, '')
        except SyntaxError as e:
            results[func] = (False, f"{e.msg} (línea relativa {e.lineno}) en '{func}'")
    return results
    
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Extrae funciones con TODO para calificar'
    )
    parser.add_argument('solution_path', help='Ruta al archivo de solución del código Python')
    parser.add_argument('student_path', help='Ruta al archivo de código Python del estudiante')
    args = parser.parse_args()
    funcs = extraer_funciones_a_calificar(args.solution_path)
    if not funcs:
        print('No hay funciones con TODO para chequear.')
    else:
        results = check_syntax(args.student_path, funcs)
        for name, (ok, msg) in results.items():
            if ok:
                print(f"{name}: sintaxis OK")
            else:
                print(f"{name}: error de sintaxis: {msg}")
