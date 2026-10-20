class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        solution = []

        for i in range(len(nums) - 2):

            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                current_sum = sort_nums[left] + sort_nums[right]
                target = -sort_nums[i]

                if current_sum == target:
                    solution.append([
                        sort_nums[i],
                        sort_nums[left],
                        sort_nums[right]
                    ])

                    while left < right and sort_nums[left] == sort_nums[left + 1]:
                        left += 1

                    while left < right and sort_nums[right] == sort_nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum > target:
                    right -= 1

                else:
                    left += 1

        return solution