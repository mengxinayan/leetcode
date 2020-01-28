class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1 or x == 2 or x == 3:
            return 1
        else:
            res = 0
            left = 0
            right = x
            mid = (left + right) // 2
            while (1):
                if mid * mid == x:
                    res = mid
                    break
                elif mid * mid > x:
                    if (mid-1) * (mid-1) <= x:
                        res = mid - 1
                        break
                    else:
                        right = mid - 1
                        mid = (left + right) // 2
                else:
                    if (mid+1) * (mid+1) > x:
                        res = mid
                        break
                    elif (mid+1) * (mid+1) == x:
                        res = mid + 1
                        break
                    else:
                        left = mid + 1
                        mid = (left + right) // 2
            return res