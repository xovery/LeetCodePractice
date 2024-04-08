class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #edge case
        if not tasks:
            return 0

        taskCount = collections.Counter(tasks).values()
        maxHeap = []
        count = 0

        #heap will pop the min value, assign "-" to change to max_heap
        for value in taskCount:
            heapq.heappush(maxHeap, -value)
        
        while maxHeap:
            remainTask = []

            for _ in range(n+1):
                
                count += 1

                if maxHeap:
                    currTaskValue = -heapq.heappop(maxHeap)
                    if currTaskValue - 1 > 0:
                        remainTask.append(currTaskValue-1)
                
                if not maxHeap and not remainTask:
                    return count

            for task in remainTask:
                heapq.heappush(maxHeap, -task)


            


                    


        