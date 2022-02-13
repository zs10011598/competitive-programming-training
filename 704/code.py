class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle_point = len(nums)//2
        initial_point = 0
        final_point = len(nums)-1
        last_middle_point = -1
        last_initial_point = -1
        last_final_point = -1
        while last_middle_point!=middle_point or last_initial_point!=initial_point or last_final_point!=final_point:
            if nums[final_point] == target:
                return final_point
            elif nums[middle_point] > target:
                last_initial_point, last_middle_point, last_final_point = initial_point, middle_point, final_point
                final_point = middle_point
                middle_point = initial_point + (middle_point-initial_point)//2
            elif nums[middle_point] < target:
                last_initial_point, last_middle_point, last_final_point = initial_point, middle_point, final_point
                initial_point = middle_point
                middle_point = middle_point + (final_point-middle_point)//2
            else:
                return middle_point

        return -1