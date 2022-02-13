class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        last_ii = -1
        last_mi = -1
        last_fi = -1
        ii = 0
        mi = len(nums)//2
        fi = len(nums) - 1
        if nums[fi] < target:
            return fi+1
        if target <= nums[ii]:
            return ii
        while last_ii != ii or last_mi != mi or last_fi != fi: 
            if nums[mi] > target:
                last_ii, last_mi, last_fi = ii, mi, fi
                fi = mi
                mi = ii + (mi-ii)//2
            elif nums[mi] < target:
                last_ii, last_mi, last_fi = ii, mi, fi
                ii = mi
                mi = mi + (fi - mi)//2
            else:
                return mi
        return fi