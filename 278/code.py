# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        last_initial_point = -1
        last_middle_point = -1
        last_final_point = -1
        initial_point = 1
        middle_point = n//2+1
        final_point = n
        isbad = True
        while last_initial_point!=initial_point or last_middle_point!=middle_point or last_final_point!=final_point:
            isbad = isBadVersion(middle_point) 
            if isbad:
                last_initial_point, last_middle_point, last_final_point = initial_point, middle_point, final_point
                final_point = middle_point
                middle_point = initial_point + (middle_point - initial_point)//2
            else:
                last_initial_point, last_middle_point, last_final_point = initial_point, middle_point, final_point
                initial_point = middle_point
                middle_point = middle_point + (final_point - middle_point)//2
        return middle_point if isbad else middle_point + 1 