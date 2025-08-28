# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.stream = nums
#         self.stream.sort()

#     def add(self, val: int) -> int:
#         index = self.getIndex(val)
#         self.stream.insert(index,val)
#         return self.stream[-self.k]        
    
#     def getIndex(self, val: int) -> int:
#         left,right = 0,len(self.stream)-1
#         while left <= right:
#             mid = (left+right)//2
#             mid_element = self.stream[mid]
#             if mid_element == val:
#                 return mid 
#             elif mid_element > val:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         return left

# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)


import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
