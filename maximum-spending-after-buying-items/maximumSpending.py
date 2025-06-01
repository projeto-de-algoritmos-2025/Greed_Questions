class Solution:
    def maxSpending(self, values):
        # Número de lojas
        lojas = len(values)

        # Número de itens por loja
        itens = len(values[0])

        combina = []  # Lista para armazenar todos os valores de itens de todas as lojas

        # Combina todos os valores em uma única lista
        for i in range(lojas):
            for j in range(itens):
                combina.append(values[i][j])

        # Ordena os valores em ordem crescente
        combina.sort()

        resultado = 0
        total_itens = lojas * itens  # Total de itens comprados (um de cada posição)

        # Para maximizar o gasto, os itens mais baratos são comprados primeiro (menor peso no multiplicador)
        # O item mais barato multiplica por 1, o segundo mais barato por 2, etc.
        for i in range(1, total_itens + 1):
            resultado += i * combina[i - 1]

        return resultado
