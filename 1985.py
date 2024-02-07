from heapq import heapify, heappop, heappush


def kthLargestNumber(nums: List[str], k: int) -> str:
    # heapq heappush: O(logn)
    # heappop: O(logn)
    # The complexity is O(n) to build the heap (heapify), then O((n-k) log n) for the pops. So it's be O((n-k) log n). Worst case O(n log n).

    heap = []
    for num in nums:
        heappush(heap, int(num))

    heapify(heap)
    n = len(heap)

    for _ in range(0, n - k):
        ele = heappop(heap)
    return str(heap[0])
