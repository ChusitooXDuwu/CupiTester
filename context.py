import ast
import argparse
from typing import List

def extraer_funciones_a_calificar(file_path: str) -> List[str]:
    """ 
    Extrae las funciones a calificar de un archivo de python, marcadas con un decorador #TODO
    
    Args:
        file_path (str): La ruta del archivo de solución.
        nivel (int): El nivel del curso al que corresponde el archivo.
        
    Returns:
        List[str]: Las funciones a calificar.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
        
    tree = ast.parse(source, filename=file_path)
    lines = source.splitlines()
    todo_funcs: List[str] = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start = node.lineno - 1
            end = getattr(node, 'end_lineno', node.lineno)
            block = lines[start:end]
            if any('TODO' in line for line in block):
                todo_funcs.append(node.name)
    return todo_funcs


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Extrae funciones con TODO para calificar'
    )
    
    parser.add_argument('solution_path', help='Ruta al archivo de código Python')
    args = parser.parse_args()

    funcs = extraer_funciones_a_calificar(args.solution_path)
    if funcs:
        for name in funcs:
            print(f" - {name}")
    else:
        print(f"No se encontraron funciones con TODO en {args.solution_path}.")
