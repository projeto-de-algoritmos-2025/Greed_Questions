import heapq 

class Solution:
    def scheduleCourse(self, courses):
        # Ordena os cursos pela data de término, em ordem crescente
        courses.sort(key=lambda x: x[1])

        max_heap = []     
        total_time = 0     

        # Itera por cada curso ordenado
        for duration, last_day in courses:
            heapq.heappush(max_heap, -duration)  # Adiciona a duração ao heap como valor negativo (simulando max-heap)
            total_time += duration               # Atualiza o tempo total gasto com os cursos escolhidos

            # Se o tempo total ultrapassa o limite (last_day), remove o curso mais longo já escolhido
            if total_time > last_day:
                # Remove o curso com maior duração (menor valor negativo)
                total_time += heapq.heappop(max_heap)  # Subtrai a maior duração (lembrando que é negativa)

        # O número de cursos no heap é o número máximo de cursos que podem ser feitos
        return len(max_heap)
