class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        solution = 0
        total = 0
        while left <= right:
            mid = (left + right) // 2
            for pile in piles:
                total += (pile + mid - 1) // mid
            if total <= h:
                solution = mid
                right = mid - 1
            else:
                left = mid + 1
            total = 0
        return solution