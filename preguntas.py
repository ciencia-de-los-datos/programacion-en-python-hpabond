"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def pregunta_01():
    with open('data.csv', 'r') as file:
        suma_segunda_columna = 0
        for line in file:
            campos = line.split('\t')
            suma_segunda_columna += int(campos[2])
    return suma_segunda_columna






def pregunta_02():
    with open('data.csv', 'r') as file:
        contador = {}
        for line in file:
            campos = line.split('\t')
            letra = campos[0]
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    resultado_pregunta_2 = sorted(contador.items())
    return resultado_pregunta_2







def pregunta_03():
    with open('data.csv', 'r') as file:
        suma_por_letra = {}
        for line in file:
            campos = line.split('\t')
            letra = campos[0]
            valor = int(campos[1])
            if letra in suma_por_letra:
                suma_por_letra[letra] += valor
            else:
                suma_por_letra[letra] = valor
    resultado_pregunta_3 = sorted(suma_por_letra.items())
    return resultado_pregunta_3








def pregunta_04():
    registros_por_mes = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            fecha = campos[2]
            mes = fecha[5:7]
            if mes in registros_por_mes:
                registros_por_mes[mes] += 1
            else:
                registros_por_mes[mes] = 1
    resultado_pregunta_4 = sorted(registros_por_mes.items())
    return resultado_pregunta_4







def pregunta_05():
    max_min_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            letra = campos[0]
            valor = int(campos[1])

            if letra in max_min_por_letra:
                max_valor, min_valor = max_min_por_letra[letra]
                max_valor = max(max_valor, valor)
                min_valor = min(min_valor, valor)
                max_min_por_letra[letra] = (max_valor, min_valor)
            else:
                max_min_por_letra[letra] = (valor, valor)
    resultado = [(letra, min_valor, max_valor) for letra, (min_valor, max_valor) in max_min_por_letra.items()]
    resultado_ordenado = sorted(resultado, key=lambda x: x[0])
    return resultado_ordenado






def pregunta_06():
    valores_por_clave = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            diccionario_codificado = campos[4]
            pares_clave_valor = diccionario_codificado.split(',')
            for par in pares_clave_valor:
                clave, valor_str = par.split(':')
                valor = int(valor_str)

                if clave in valores_por_clave:
                    min_valor, max_valor = valores_por_clave[clave]
                    max_valor = max(max_valor, valor)
                    min_valor = min(min_valor, valor)
                    valores_por_clave[clave] = (min_valor, max_valor)
                else:
                    valores_por_clave[clave] = (valor, valor)
    resultado = [(clave, min_valor, max_valor) for clave, (min_valor, max_valor) in valores_por_clave.items()]
    resultado_ordenado_pregunta_06 = sorted(resultado, key=lambda x: x[0])
    return resultado_ordenado_pregunta_06






def pregunta_07():
    valores_letras = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            valor_col2 = int(campos[1])
            letra_col1 = campos[0]

            if valor_col2 in valores_letras:
                valores_letras[valor_col2].append(letra_col1)
            else:
                valores_letras[valor_col2] = [letra_col1]

    resultado = [(valor, letras) for valor, letras in valores_letras.items()]

    resultado_ordenado = sorted(resultado, key=lambda x: x[0])

    return resultado_ordenado







def pregunta_08():
    valores_letras = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            valor_col2 = int(campos[1])
            letra_col1 = campos[0]
            if valor_col2 in valores_letras:
                valores_letras[valor_col2].append(letra_col1)
            else:
                valores_letras[valor_col2] = [letra_col1]
    resultado = sorted([(valor, sorted(list(set(letras)))) for valor, letras in valores_letras.items()], key=lambda x: x[0])
    return resultado









def pregunta_09():
    contador_claves = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            columna_5 = campos[4].split(',')

            for par in columna_5:
                clave, valor = par.split(':')
                clave = clave.strip()  
                if clave in contador_claves:
                    contador_claves[clave] += 1
                else:
                    contador_claves[clave] = 1
    resultado_ordenado = sorted(contador_claves.items(), key=lambda x: x[0])
    return dict(resultado_ordenado)
    







def pregunta_10():

    resultados = []

    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            letra = campos[0]
            elementos_col4 = len(campos[3].split(','))
            elementos_col5 = len(campos[4].split(','))

            resultado = (letra, elementos_col4, elementos_col5)

            resultados.append(resultado)

    return resultados




def pregunta_11():
    suma_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            letra_col4 = campos[3].split(',')
            valor_col2 = int(campos[1])

            for letra in letra_col4:
                letra = letra.strip()  
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_col2
                else:
                    suma_por_letra[letra] = valor_col2

    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada




def pregunta_12():
    resultado = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    with open('data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')

            if len(campos) >= 5:
                letra_col1 = campos[0]
                valores_col5 = campos[4].split(',')

                for valor in valores_col5:
                    clave, cantidad = valor.split(':')
                    if clave.strip().isalpha() and cantidad.strip().isdigit():
                        resultado[letra_col1] += int(cantidad)

    return resultado
