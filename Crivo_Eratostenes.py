import mysql.connector

def crivo_erastostenes(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  # 0 e 1 não são primos

    for i in range(2, int(limite ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, limite + 1, i):
                primos[j] = False

    numeros_primos = [num for num, primo in enumerate(primos) if primo]
    return numeros_primos


def primo_tuplas(primos):
    tuplas = []
    for i in range(len(primos)):
        for j in range(i+1, len(primos)):
            pi = primos[i]
            pj = primos[j]
            produto = pi * pj
            tupla = (pi, pj, produto)
            tuplas.append(tupla)
    return tuplas

primos = crivo_erastostenes(100)
tuplas = primo_tuplas(primos)
# Imprimir as tuplas geradas
for tupla in tuplas:
    print(tupla)



def insertDatabase(tuplas):
    cnx = mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='seu_banco_de_dados'
    )


    cursor = cnx.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tabela_primos (Pi INT, Pj INT, Produto INT)")

    for tupla in tuplas:
        pi, pj, produto = tupla
        query = "INSERT INTO tabela_primos (Pi, Pj, Produto) VALUES (%s, %s, %s)"
        values = (pi, pj, produto)
        cursor.execute(query, values)

    cnx.commit()


    cursor.close()
    cnx.close()
