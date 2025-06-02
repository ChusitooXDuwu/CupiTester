# CupiTester

Pipeline Actual:

1. Context.py: Revisa el archivo de solución e identifica cuales son las funciones que tienen un #TODO asociado para la calificación.

2. Syntax.py: Revisa si las funciones a calificar del context, tienen errores de syntaxis, e indica el error si es necesario.

3. Forbidden.py: Para aquellas funciones que no tienen error de syntaxis, revisa si las funciones usan operadores fuera del nivel del curso, y específica cuales.

4. Test.py: Para las funnciones validas del punto anterior, se corren los doctest asociados de la solución en el archivo del estudiante, y se indica cuales no pasaron.
