from typing import List

class Solution:
    def findMinimumTime(self, tarefas: List[List[int]]) -> int:
        if not tarefas:
            return 0

        tarefas.sort(key=lambda x: x[1])
        
        max_fim = max(t[1] for t in tarefas)
        ligado = [False] * (max_fim + 1)
        tempo_total = 0
        
        for inicio, fim, duracao in tarefas:
            cobertos = 0
            for t in range(inicio, fim + 1):
                if ligado[t]:
                    cobertos += 1

            faltam = duracao - cobertos
            t = fim
            while faltam > 0 and t >= inicio:
                if not ligado[t]:
                    ligado[t] = True
                    tempo_total += 1
                    faltam -= 1
                t -= 1
        
        return tempo_total