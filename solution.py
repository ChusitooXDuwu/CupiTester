#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CupiDetectives
"""

import doctest

def crear_sospechoso(codigo: int, nombre: str, edad: int, altura: float, pantalon: str, camisa: str, usaba_gafas: bool, salon: str, coartada_confirmada: bool, huellas_confirmadas: bool) -> dict:
    """
    Crea un diccionario con la información de un sospechoso en el caso de la desaparición de Edouardinho.
    
    Las llaves del diccionario a crear y retornar deben llevar como nombre exactamente el mismo nombre de su parámetro respectivo.
    Por ejemplo: "codigo": codigo, "nombre": nombre, etc.
        
    Parámetros:
        codigo (int): Código único del sospechoso.
        nombre (str): Nombre del sospechoso.
        edad (int): Edad en años.
        altura (float): Altura en metros.
        pantalon (str): Color del pantalón.
        camisa (str): Color de la camisa.
        usaba_gafas (bool): True si el sospechoso llevaba gafas, False en caso contrario.
        salon (str): Salón donde fue visto el sospechoso al momento del incidente (ejemplo: ML-515).
        coartada_confirmada (bool): True si el sospechoso tiene una coartada que fue confirmada por CupiDetectives, False en caso contrario.
        huellas_confirmadas (bool): True si las huellas digitales del sospechoso coinciden con las encontradas en el salón donde ocurrió el incidente, False en caso contrario.

    Retorna:
        dict: Diccionario con la información del sospechoso.
    
    >>> crear_sospechoso(1, "Juan", 25, 1.75, "Azul; Jeans; Largo Completo", "Blanca; Cuello redondo; Regular Fit", True, "ML-610", True, True)
    {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': True, 'huellas_confirmadas': True}
    """
    # TODO 1 - Solución
    return {
        "codigo": codigo,
        "nombre": nombre,
        "edad": edad,
        "altura": altura,
        "pantalon": pantalon,
        "camisa": camisa,
        "pantalon": pantalon,
        "camisa": camisa,
        "usaba_gafas": usaba_gafas,
        "salon": salon,
        "coartada_confirmada": coartada_confirmada,
        "huellas_confirmadas": huellas_confirmadas
    }

#doctest.run_docstring_examples(crear_sospechoso, globals(), verbose=True)


def crear_perfil_culpable(edad_estimada: int, altura_estimada: float, pantalon: str, camisa: str, usaba_gafas: bool, salon_incidente: str) -> dict:
    """
    Crea un diccionario con el perfil del presunto culpable.
    Esta información fue recolectada en entrevista con Séneca, principal testigo del incidente.
    
    Las llaves del diccionario a crear deben llevar como nombre exactamente el mismo nombre de su parámetro respectivo.
    Por ejemplo: "edad_estimada": edad_estimada, "altura_estimada": altura_estimada, etc.

    Parámetros:
        edad_estimada (int): Edad máxima estimada del culpable.
        altura_estimada (float): Altura estimada en metros del culpable.
        pantalon (str): Color del pantalón del culpable.
        camisa (str): Color de la camisa del culpable.
        usaba_gafas (bool): True si el culpable llevaba gafas, False en caso contrario.
        salon_incidente (str): Salón en donde Séneca vio al culpable y en donde desapareció Edouardinho (ejemplo: ML-610).

    Retorna:
        dict: Diccionario con el perfil del presunto culpable.
    
    >>> crear_perfil_culpable(22, 1.75, "Negro; Bermuda; Largo Pescador", "Blanca; Cuello redondo; Regular Fit", True, "ML-610")
    {'edad_estimada': 22, 'altura_estimada': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon_incidente': 'ML-610'}
    """
    # TODO 2 - Solución
    return {
        "edad_estimada": edad_estimada,
        "altura_estimada": altura_estimada,
        "pantalon": pantalon,
        "camisa": camisa,
        "pantalon": pantalon,
        "camisa": camisa,
        "usaba_gafas": usaba_gafas,
        "salon_incidente": salon_incidente,
    }

#doctest.run_docstring_examples(crear_perfil_culpable, globals(), verbose=True)

def buscar_por_codigo(codigo: int, s1: dict, s2: dict, s3: dict, s4: dict) -> dict:
    """
    Busca a un sospechoso por su código. El código de un sospechoso es único.

    Parámetros:
        codigo (int): Código del sospechoso a buscar.
        s1 (dict): Diccionario que contiene la información del primer sospechoso.
        s2 (dict): Diccionario que contiene la información del segundo sospechoso.
        s3 (dict): Diccionario que contiene la información del tercer sospechoso.
        s4 (dict): Diccionario que contiene la información del cuarto sospechoso.
        
    Retorno:            
        dict: Diccionario con la información del sospechoso cuyo código coincida con el código dado.
              Retorna un diccionario vacío si ningún sospechoso tiene el código dado. 
    
    # Caso código s1
    >>> buscar_por_codigo(1, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 21, 'altura': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Eduardinho', 'edad': 34, 'altura': 1.99, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Seneca', 'edad': 18, 'altura': 1.65, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True})  
    {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}
    
    # Caso código s2
    >>> buscar_por_codigo(2,
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 21, 'altura': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Eduardinho', 'edad': 34, 'altura': 1.99, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Seneca', 'edad': 18, 'altura': 1.65, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True}) 
    {'codigo': 2, 'nombre': 'Eric', 'edad': 21, 'altura': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True}
    
    #Caso código s3
    >>> buscar_por_codigo(3,
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 21, 'altura': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Eduardinho', 'edad': 34, 'altura': 1.99, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Seneca', 'edad': 18, 'altura': 1.65, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True}) 
    {'codigo': 3, 'nombre': 'Eduardinho', 'edad': 34, 'altura': 1.99, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True}
    
    #Caso código s4
    >>> buscar_por_codigo(4, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 21, 'altura': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Eduardinho', 'edad': 34, 'altura': 1.99, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Seneca', 'edad': 18, 'altura': 1.65, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True}) 
    {'codigo': 4, 'nombre': 'Seneca', 'edad': 18, 'altura': 1.65, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True}
    
    #Caso Ninguno
    >>> buscar_por_codigo(5,
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 21, 'altura': 1.75, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Eduardinho', 'edad': 34, 'altura': 1.99, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Seneca', 'edad': 18, 'altura': 1.65, 'pantalon': 'Negro; Bermuda; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-610', 'coartada_confirmada': False, 'huellas_confirmadas': True}) 
    {}
    """
    # TODO 3 - Solución
    sospechoso = {}

    if s1["codigo"] == codigo:
        sospechoso = s1
    elif s2["codigo"] == codigo:
        sospechoso = s2
    elif s3["codigo"] == codigo:
        sospechoso = s3
    elif s4["codigo"] == codigo:
        sospechoso = s4

    return sospechoso


#doctest.run_docstring_examples(buscar_por_codigo, globals(), verbose=True)


def filtrar_sospechosos_por_ubicacion(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> str:
    """
    Filtrar los códigos de los sospechosos que estaban en el salón donde fue visto el presunto culpable.
    
    Nota: Recuerde que un código es del tipo `int`. Para concatenarlo, debe convertirlo primero a string, usando la función de Python `str()`.

    Parámetros:
        perfil_culpable (dict): Diccionario con el perfil del presunto culpable. 
            De este diccionario se debe extraer el salón donde fue visto el presunto culpable al momento del incidente.
            
        s1 (dict): Diccionario que contiene la información del primer sospechoso.
        s2 (dict): Diccionario que contiene la información del segundo sospechoso.
        s3 (dict): Diccionario que contiene la información del tercer sospechoso.
        s4 (dict): Diccionario que contiene la información del cuarto sospechoso.
        
    Retorno:
        str: Códigos de los sospechosos que se encontraban en el salón donde fue visto el presunto culpable, separados por coma.   
               Por ejemplo, si únicamente el sospechoso con el código 1 estuvo en salón, se retornaría: "1"
                 Si los sospechosos idenficados con los códigos 1 y 2, estaban en el salón, se retornaría: "1, 2"
             Retorna "Ninguno" si ningún sospechoso estaba en ese salón.
             
    #Caso solo 1
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1'

    #Caso solo 2
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-410"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2'

    #Caso solo 3
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-310"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '3'

    #Caso solo 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-210"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '4'

    #Caso 1 y 2
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2'

    #Caso 1 y 3
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 3'

    #Caso 1 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 4'

    #Caso 2 y 3
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-410"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 3'

    #Caso 2 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-410"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 4'

    #Caso 3 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-310"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '3, 4'

    #Caso 1, 2 y 3
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 3'

    #Caso 1, 2 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 4'

    #Caso 1, 3 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 3, 4'

    #Caso 2, 3 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-410"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 3, 4'

    #Caso 1, 2, 3 y 4
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 3, 4'

    #Caso Ninguno
    >>> filtrar_sospechosos_por_ubicacion({"salon_incidente": "ML-610"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    'Ninguno'
    """
    # TODO 4 - Solución
    salon_incidente = perfil_culpable["salon_incidente"]

    sospechosos_por_ubicacion = ""
    
    if s1["salon"] == salon_incidente:
        sospechosos_por_ubicacion += str(s1["codigo"])
    
    if s2["salon"] == salon_incidente:
        if sospechosos_por_ubicacion != "":
            sospechosos_por_ubicacion += ", "
        sospechosos_por_ubicacion += str(s2["codigo"])
    
    if s3["salon"] == salon_incidente:
        if sospechosos_por_ubicacion != "":
            sospechosos_por_ubicacion += ", "
        sospechosos_por_ubicacion += str(s3["codigo"])
    
    if s4["salon"] == salon_incidente:
        if sospechosos_por_ubicacion != "":
            sospechosos_por_ubicacion += ", "
        sospechosos_por_ubicacion += str(s4["codigo"])

    if sospechosos_por_ubicacion == "":
        sospechosos_por_ubicacion = "Ninguno"

    return sospechosos_por_ubicacion

#doctest.run_docstring_examples(filtrar_sospechosos_por_ubicacion, globals(), verbose=True)


def filtrar_sospechosos_por_vestimenta(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> str:
    """
    Filtra los códigos de los sospechosos que coincidan con el perfil del presunto culpable, teniendo en cuenta el color de sus pantalones, el color de su camisa y el uso de gafas.
    
    Nota: Recuerde que un código es del tipo `int`. Para concatenarlo, debe convertirlo primero a string, usando la función de Python `str()`.

    Parámetros:
        perfil_culpable (dict): Diccionario con el perfil del presunto culpable. 
            De este diccionario se debe extraer el color de pantalón, color de camisa y si usaba gafas el presunto culpable.
            
        s1 (dict): Diccionario que contiene la información del primer sospechoso.
        s2 (dict): Diccionario que contiene la información del segundo sospechoso.
        s3 (dict): Diccionario que contiene la información del tercer sospechoso.
        s4 (dict): Diccionario que contiene la información del cuarto sospechoso.
        
    Retorno:
        str: Códigos de los sospechosos que cumplen con las tres condiciones de vestimenta, separados por coma, por ejemplo: "1, 3"
             Retorna "Ninguno" si ningún sospechoso cumple con las condiciones.
             
    #Caso solo 1
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Azul',"camisa": 'Azul',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Morado; Leggings; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1'

    #Caso solo 2
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Morado',"camisa": 'Morado',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Morado; Leggings; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2'

    #Caso solo 3
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Morado; Leggings; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '3'

    #Caso solo 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Blanca',"camisa": 'Blanca',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Morado; Leggings; Largo Pescador', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '4'

    #Caso 1 y 2
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Azul',"camisa": 'Azul',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2'

    #Caso 1 y 3
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Azul',"camisa": 'Azul',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 3'

    #Caso 1 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Azul',"camisa": 'Azul',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 4'

    #Caso 2 y 3
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 3'

    #Caso 2 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 4'

    #Caso 3 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Blanca',"camisa": 'Blanca',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Azul; Cuello polo; Oversize', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Blanca; Cargo; Largo Corto', 'camisa': 'Blanca; Cuello redondo; Regular Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '3, 4'

    #Caso 1, 2 y 3
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 3'

    #Caso 1, 2 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 4'

    #Caso 1, 3 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 3, 4'

    #Caso 2, 3 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Morado; Cuello tortuga; Tailored Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 3, 4'

    #Caso 1, 2, 3 y 4
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": False,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 3, 4'

    #Caso Ninguno
    >>> filtrar_sospechosos_por_vestimenta(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 25, 'altura': 1.67, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 24, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 0.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    'Ninguno'
    """
    # TODO 5 - Solución
    pantalon = perfil_culpable["pantalon"]
    camisa = perfil_culpable["camisa"]
    pantalon = perfil_culpable["pantalon"]
    camisa = perfil_culpable["camisa"]
    usaba_gafas = perfil_culpable["usaba_gafas"]

    sospechosos_por_vestimenta = ""

    if pantalon in s1["pantalon"] and camisa in s1["camisa"] and s1["usaba_gafas"] == usaba_gafas:
        sospechosos_por_vestimenta += str(s1["codigo"])
    
    if pantalon in s2["pantalon"] and camisa in s2["camisa"] and s1["usaba_gafas"] == usaba_gafas :
        if sospechosos_por_vestimenta != "":
            sospechosos_por_vestimenta += ", "
        sospechosos_por_vestimenta += str(s2["codigo"])

    if pantalon in s3["pantalon"] and camisa in s3["camisa"] and s3["usaba_gafas"] == usaba_gafas:
        if sospechosos_por_vestimenta != "":
            sospechosos_por_vestimenta += ", "
        sospechosos_por_vestimenta += str(s3["codigo"])

    if pantalon in s4["pantalon"] and camisa in s4["camisa"] and s4["usaba_gafas"] == usaba_gafas:
        if sospechosos_por_vestimenta != "":
            sospechosos_por_vestimenta += ", "
        sospechosos_por_vestimenta += str(s4["codigo"])

    if sospechosos_por_vestimenta == "":
        sospechosos_por_vestimenta = "Ninguno"

    return sospechosos_por_vestimenta

#doctest.run_docstring_examples(filtrar_sospechosos_por_vestimenta, globals(), verbose=True)


def filtrar_sospechosos_por_edad_altura(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> str:
    """
    Filtra los códigos de los sospechosos cuya edad es menor o igual a la edad máxima estimada del culpable y 
    cuya altura en metros está en el rango de la altura estimada ± 10cm. 
    
    Por ejemplo, si la altura estimada es 1.80m, se permite un margen de ±10 cm. 
    Esto significaría que el rango válido de altura es de 1.70m a 1.90m (incluyendo a 1.70 y a 1.90).
    
    Nota: Recuerde que un código es del tipo `int`. Para concatenarlo, debe convertirlo primero a string, usando la función de Python `str()`.

    Parámetros:
        perfil_culpable (dict): Diccionario con el perfil del presunto culpable.
            De este diccionario se debe extraer la edad y altura estimadas del presunto culpable.
            
        s1 (dict): Diccionario que contiene la información del primer sospechoso.
        s2 (dict): Diccionario que contiene la información del segundo sospechoso.
        s3 (dict): Diccionario que contiene la información del tercer sospechoso.
        s4 (dict): Diccionario que contiene la información del cuarto sospechoso.
    
    Retorno:
        str: Códigos de los sospechosos que cumplen con las dos condiciones sobre edad y altura, separados por coma, por ejemplo: "2, 4"
             Retorna "Ninguno" si ningún sospechoso cumple con ambas condiciones.
    
    #Caso solo 1
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 18,"altura_estimada": 1.75,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.45, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1'

    #Caso solo 2
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 21,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.74, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.45, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2'

    #Caso solo 3
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 2.96,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.74, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 2.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.45, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '3'

    #Caso solo 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.44,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.74, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 2.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.45, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '4'

    #Caso 1 y 2
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 2.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.45, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2'

    #Caso 1 y 3
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.45, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 3'

    #Caso 1 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 4'

    #Caso 2 y 3
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.05,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 3'

    #Caso 2 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.05,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 4'

    #Caso 3 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.05,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '3, 4'

    #Caso 1, 2 y 3
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.90,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.05, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 3'

    #Caso 1, 2 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.96, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 4'

    #Caso 1, 3 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.65, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 3, 4'

    #Caso 2, 3 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.65, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.85, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '2, 3, 4'

    #Caso 1, 2, 3 y 4
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    '1, 2, 3, 4'

    #Caso Ninguno
    >>> filtrar_sospechosos_por_edad_altura(
    ... {"edad_estimada": 41,"altura_estimada": 2.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    'Ninguno'
    """
    # TODO 6 - Solución
    edad_maxima_culpable = perfil_culpable["edad_estimada"]
    altura_estimada_culpable = perfil_culpable["altura_estimada"]
    DELTA_ALTURA = 0.10

    sospechosos_por_edad_altura = ""
    
    altura_min = altura_estimada_culpable - DELTA_ALTURA
    altura_max = altura_estimada_culpable + DELTA_ALTURA
    
    if s1["edad"] <= edad_maxima_culpable and altura_min <= s1["altura"] <= altura_max:
        sospechosos_por_edad_altura += str(s1["codigo"])
    
    if s2["edad"] <= edad_maxima_culpable and altura_min <= s2["altura"] <= altura_max:
        if sospechosos_por_edad_altura:
            sospechosos_por_edad_altura += ", "
        sospechosos_por_edad_altura += str(s2["codigo"])
    
    if s3["edad"] <= edad_maxima_culpable and altura_min <= s3["altura"] <= altura_max:
        if sospechosos_por_edad_altura:
            sospechosos_por_edad_altura += ", "
        sospechosos_por_edad_altura += str(s3["codigo"])
    
    if s4["edad"] <= edad_maxima_culpable and altura_min <= s4["altura"] <= altura_max:
        if sospechosos_por_edad_altura:
            sospechosos_por_edad_altura += ", "
        sospechosos_por_edad_altura += str(s4["codigo"])
    
    if sospechosos_por_edad_altura == "":
        sospechosos_por_edad_altura = "Ninguno"
    
    return sospechosos_por_edad_altura

#doctest.run_docstring_examples(filtrar_sospechosos_por_edad_altura, globals(), verbose=True)




def calcular_probabilidad_de_culpabilidad(codigo: int, perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> float:
    """
    Calcula la probabilidad de que un sospechoso sea el culpable según su ubicación, vestimenta y características físicas.

    Se usa la fórmula F1:
    
    probabilidad = (a * 0.45) + (b * 0.35) + (c * 0.20)
    
        Donde:
            a = 1 si el sospechoso estuvo en el salón reportado por Séneca, 0 en caso contrario.
            b = 1 si el sospechoso llevaba la vestimenta descrita por Séneca, 0 en caso contrario.
            c = 1 si la edad y altura del sospechoso son similares a las estimadas por Séneca, 0 en caso contrario.
            Los valores 0.45, 0.35 y 0.20 representan pesos fijos que reflejan la importancia relativa de cada factor para determinar
            la probabilidad de culpabilidad.
            
    Nota: Recuerde que un código es del tipo `int`. Si desea convertirlo a string, debe usar la función de Python `str()`.

    Parámetros:
        codigo (int): Código del sospechoso.
        perfil_culpable (dict): Diccionario con el perfil del presunto culpable.
        s1 (dict): Diccionario que contiene la información del primer sospechoso.
        s2 (dict): Diccionario que contiene la información del segundo sospechoso.
        s3 (dict): Diccionario que contiene la información del tercer sospechoso.
        s4 (dict): Diccionario que contiene la información del cuarto sospechoso.

    Retorna:
        float: Probabilidad de que el sospechoso sea el culpable, redondeada a 2 decimales.
               Retorna 0.0 si el código no le pertenece a ningún sospechoso o si el sospechoso no cumple con ningún criterio considerado en la fórmula.
    
    #Caso solo ubicación
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 2.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 50, 'altura': 1.86, 'pantalon': 'Marron; Bermuda; Largo Pescador', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.45

    #Caso solo vestimenta
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 2.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 50, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.35

    #Caso solo edad-altura
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Marron; Bermuda; Largo Pescador', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.2

    #Caso ubicación y vestimenta
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 81, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.8

    #Caso ubicación y edad-altura
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Marron; Bermuda; Largo Pescador', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.65

    #Caso vestimenta y edad-altura
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.55

    #Caso Probabilidad 1
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    1.0


    #Caso probabilidad 0
    >>> calcular_probabilidad_de_culpabilidad(
    ... 1,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 81, 'altura': 1.86, 'pantalon': 'Marron; Bermuda; Largo Pescador', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.0


    #Caso Ninguno
    >>> calcular_probabilidad_de_culpabilidad(
    ... 6,
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 19, 'altura': 1.89, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 31, 'altura': 1.75, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-310', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.95, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-210', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    0.0
    """
    # TODO 7 - Solución
    probabilidad = 0.0
    sospechoso = buscar_por_codigo(codigo, s1, s2, s3, s4)

    if sospechoso != {}:
        sospechosos_por_ubicacion = filtrar_sospechosos_por_ubicacion(perfil_culpable, s1, s2, s3, s4)
        sospechosos_por_vestimenta = filtrar_sospechosos_por_vestimenta(perfil_culpable, s1, s2, s3, s4)
        sospechosos_por_edad_altura = filtrar_sospechosos_por_edad_altura(perfil_culpable, s1, s2, s3, s4)

        PESO_UBICACION = 0.45
        PESO_VESTIMENTA = 0.35
        PESO_EDAD_ALTURA = 0.20

        a = 0
        if str(sospechoso["codigo"]) in sospechosos_por_ubicacion:
            a = 1

        b = 0
        if str(sospechoso["codigo"]) in sospechosos_por_vestimenta:
            b = 1

        c = 0
        if str(sospechoso["codigo"]) in sospechosos_por_edad_altura:
            c = 1

        probabilidad = (a * PESO_UBICACION) + (b * PESO_VESTIMENTA) + (c * PESO_EDAD_ALTURA)

    return round(probabilidad, 2)

#doctest.run_docstring_examples(calcular_probabilidad_de_culpabilidad, globals(), verbose=True)

def ajustar_probabilidad(sospechosos: str, criterio:str, peso_maximo:float, factor_decrecimiento: float)->float:
    """
    Ajusta la probabilidad de culpabilidad de los sospechosos según la cantidad de sospechosos que cumplen con un criterio.

    La probabilidad de culpabilidad de los sospechosos se ajusta de acuerdo a la cantidad de sospechosos que cumplen con un criterio.
    Si hay 1 sospechoso que cumple con el criterio, la probabilidad se mantiene igual.
    Si hay 2 sospechosos que cumplen con el criterio, la probabilidad se reduce en `factor_decrecimiento`.
    Si hay 3 sospechosos que cumplen con el criterio, la probabilidad se reduce en `2*factor_decrecimiento`.
    Si hay 4 sospechosos que cumplen con el criterio, la probabilidad se reduce en `3*factor_decrecimiento`.

    Si la probabilidad ajustada es menor a un valor mínimo, se ajusta a ese valor mínimo.

    Parámetros:
        peso_maximo (float): Peso máximo de la probabilidad.
        sospechosos (str): Códigos de los sospechosos que cumplen con el criterio.
        criterio (str): Criterio que se está evaluando.
        factor_decrecimiento (float): Factor de decrecimiento de la probabilidad.
    
    Retorna:
        float: Probabilidad ajustada de culpabilidad de los sospechosos, redondeado a 2 decimales

    #Caso ubicación, 1 culpable
    >>> ajustar_probabilidad("1", "ubicacion", 0.45, 0.12)
    0.45

    #Caso ubicación, 2 culpables
    >>> ajustar_probabilidad("1, 2", "ubicacion", 0.45, 0.12)
    0.33

    #Caso ubicación, 3 culpables
    >>> ajustar_probabilidad("1, 2, 3", "ubicacion", 0.45, 0.12)
    0.21

    #Caso ubicación, 4 culpables (Probabilidad Minima)
    >>> ajustar_probabilidad("1, 2, 3, 4", "ubicacion", 0.45, 0.12)
    0.1

    #Caso vestimenta, 1 culpable
    >>> ajustar_probabilidad("1", "vestimenta", 0.35, 0.10)
    0.35

    #Caso vestimenta, 2 culpables
    >>> ajustar_probabilidad("1, 2", "vestimenta", 0.35, 0.10)
    0.25

    #Caso vestimenta, 3 culpables (Probabilidad Minima)
    >>> ajustar_probabilidad("1, 2, 3", "vestimenta", 0.35, 0.10)
    0.2

    #Caso vestimenta, 4 culpables (Probabilidad Minima)
    >>> ajustar_probabilidad("1, 2, 3, 4", "vestimenta", 0.35, 0.10)
    0.2

    #Caso edad-altura, 1 culpable
    >>> ajustar_probabilidad("1", "edad_altura", 0.20, 0.05)
    0.2

    #Caso edad-altura, 2 culpables
    >>> ajustar_probabilidad("1, 2", "edad_altura", 0.20, 0.05)
    0.15

    #Caso edad-altura, 3 culpables
    >>> ajustar_probabilidad("1, 2, 3", "edad_altura", 0.20, 0.05)
    0.1

    #Caso edad-altura, 4 culpables 
    >>> ajustar_probabilidad("1, 2, 3, 4", "edad_altura", 0.20, 0.05)
    0.05
    """

    if criterio == "ubicacion":
        minima_probabilidad = 0.10
    elif criterio == "vestimenta":
        minima_probabilidad = 0.20
    elif criterio == "edad_altura":
        minima_probabilidad = 0.05

    tamanio = len(sospechosos)

    probabilidad_ajustada = peso_maximo

    if tamanio == 1:
        probabilidad_ajustada = peso_maximo
    elif tamanio == 4:
        probabilidad_ajustada = peso_maximo - factor_decrecimiento
    elif tamanio == 7:
        probabilidad_ajustada = peso_maximo - 2*factor_decrecimiento
    elif tamanio == 10:
        probabilidad_ajustada = peso_maximo - 3*factor_decrecimiento

    if probabilidad_ajustada < minima_probabilidad:
        probabilidad_ajustada = minima_probabilidad
    
    return round(probabilidad_ajustada,2)
#doctest.run_docstring_examples(ajustar_probabilidad, globals(), verbose=True)


def encontrar_sospechoso_con_mayor_probabilidad(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> dict:
    """
    Busca al sospechoso con la mayor probabilidad de ser culpable.
    
    Finalmente, la brigada CupiDetectives ha terminado el proceso de revisión de coartadas de los sospechosos.
    Más importante aún, se ha terminado el proceso de confirmación de huellas dactilares. 
    Dada esta nueva información:

    - Si hay empate en la probabilidad, se elige al sospechoso sin coartada confirmada.
      - Si aún hay empate, se elige al sospechoso cuyas huellas digitales hayan sido confirmadas.
        - Si el empate persiste, por simplicidad se elige al primer sospechoso evaluado en orden de ingreso a la función (s1 a s4).

    Parámetros:
        perfil_culpable (dict): Diccionario con el perfil del presunto culpable. 
        s1 (dict): Diccionario que contiene la información del primer sospechoso.
        s2 (dict): Diccionario que contiene la información del segundo sospechoso.
        s3 (dict): Diccionario que contiene la información del tercer sospechoso.
        s4 (dict): Diccionario que contiene la información del cuarto sospechoso.
            De cada diccionario se debe extraer si el sospechoso tiene su coartada y huellas confirmadas.

    Retorna:
        dict: Diccionario del sospechoso con la mayor probabilidad de culpabilidad, según todo lo anteriormente descrito.
   
    #Caso solo 1
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 81, 'altura': 1.89, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.75, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.95, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso solo 2
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso solo 3
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso solo 4
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1 y 2, coartada confirmada s1
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1 y 2, coartada confirmada s2
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True})
    {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1 y 2, empate coartada confirmada, huellas confirmadas s1
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1 y 2, empate coartada confirmada, huellas confirmadas s2
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True})
    {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1 y 2, empate coartada confirmada, empate huellas confirmadas
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 81, 'altura': 1.86, 'pantalon': 'Azul; Jeans; Largo Completo', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': False, 'salon': 'ML-410', 'coartada_confirmada': True, 'huellas_confirmadas': True})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False}

    #Caso Empate 1, 2, 3 y 4, coartada confirmada s1
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False}

    #Caso Empate 1, 2, 3 y 4, coartada confirmada s2
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False})
    {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False}

    #Caso Empate 1, 2, 3 y 4, coartada confirmada s3
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False})
    {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False}

    #Caso Empate 1, 2, 3 y 4, coartada confirmada s4
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': True, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False})
    {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False}

    #Caso Empate 1, 2, 3 y 4, empate coartada confirmada, huellas confirmadas s1
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1, 2, 3 y 4, empate coartada confirmada, huellas confirmadas s2
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False})
    {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1, 2, 3 y 4, empate coartada confirmada, huellas confirmadas s3
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False})
    {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1, 2, 3 y 4, empate coartada confirmada, huellas confirmadas s4
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}

    #Caso Empate 1, 2, 3 y 4, empate coartada confirmada, empate huellas confirmadas (Empate Huellas False)
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': False}

    #Caso Empate 1, 2, 3 y 4, empate coartada confirmada, empate huellas confirmadas (Empate Huellas True)
    >>> encontrar_sospechoso_con_mayor_probabilidad(
    ... {"edad_estimada": 41,"altura_estimada": 1.85,"pantalon": 'Verde',"camisa": 'Verde',"usaba_gafas": True,"salon_incidente": "ML-510"}, 
    ... {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 2, 'nombre': 'Eric', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 3, 'nombre': 'Gabe', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True},
    ... {'codigo': 4, 'nombre': 'Chu', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True})
    {'codigo': 1, 'nombre': 'Juan', 'edad': 18, 'altura': 1.86, 'pantalon': 'Verde; Jogger; Largo Capri', 'camisa': 'Verde; Cuello V; Slim Fit', 'usaba_gafas': True, 'salon': 'ML-510', 'coartada_confirmada': False, 'huellas_confirmadas': True}
    """
    # TODO 8 - Solución
    probabilidad_s1 = calcular_probabilidad_de_culpabilidad(s1["codigo"], perfil_culpable, s1, s2, s3, s4)
    probabilidad_s2 = calcular_probabilidad_de_culpabilidad(s2["codigo"], perfil_culpable, s1, s2, s3, s4)
    probabilidad_s3 = calcular_probabilidad_de_culpabilidad(s3["codigo"], perfil_culpable, s1, s2, s3, s4)
    probabilidad_s4 = calcular_probabilidad_de_culpabilidad(s4["codigo"], perfil_culpable, s1, s2, s3, s4)
    
    culpable = s1
    max_probabilidad = probabilidad_s1

    if probabilidad_s2 > max_probabilidad:
        max_probabilidad = probabilidad_s2
        culpable = s2
    elif probabilidad_s2 == max_probabilidad:
        if not s2["coartada_confirmada"] and culpable["coartada_confirmada"]:
            culpable = s2
        elif s2["coartada_confirmada"] == culpable["coartada_confirmada"] and s2["huellas_confirmadas"] != culpable["huellas_confirmadas"] and s2["huellas_confirmadas"]:
            culpable = s2

    if probabilidad_s3 > max_probabilidad:
        max_probabilidad = probabilidad_s3
        culpable = s3
    elif probabilidad_s3 == max_probabilidad:
        if not s3["coartada_confirmada"] and culpable["coartada_confirmada"]:
            culpable = s3
        elif s3["coartada_confirmada"] == culpable["coartada_confirmada"] and s3["huellas_confirmadas"] != culpable["huellas_confirmadas"] and s3["huellas_confirmadas"]: 
            culpable = s3

    if probabilidad_s4 > max_probabilidad:
        max_probabilidad = probabilidad_s4
        culpable = s4
    elif probabilidad_s4 == max_probabilidad:
        if not s4["coartada_confirmada"] and culpable["coartada_confirmada"]:
            culpable = s4
        elif s4["coartada_confirmada"] == culpable["coartada_confirmada"] and s4["huellas_confirmadas"] != culpable["huellas_confirmadas"] and s4["huellas_confirmadas"]:
            culpable = s4

    return culpable

#doctest.run_docstring_examples(encontrar_sospechoso_con_mayor_probabilidad, globals(), verbose=True)

# Todos los tests:
#doctest.testmod(verbose=True)
