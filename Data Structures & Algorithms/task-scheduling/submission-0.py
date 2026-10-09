class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #use a queue + heap algo, you need to get the frequencies of each task
        #max heap for most frequent tasks to go through

        freq = Counter(tasks)

        heap = [(-count, task) for task, count in freq.items()]

        heapq.heapify(heap)

        queue = deque()

        count = 0

        while heap or queue:

            if queue and count > queue[0][2]:
                heapq.heappush(heap, queue.popleft())

            if not heap:
                count += 1
                continue

            task = heapq.heappop(heap)

            if task[0] < 0:
                queue.append((task[0] + 1, task[1], count+n))
                count += 1

        return count - n


        

        
