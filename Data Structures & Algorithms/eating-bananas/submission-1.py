class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # how many minimum banana that can consume all banana per hour within k hour limit
        # brute force try 1 banana until max banana pile count
        # because eating more than max banana pile will wait anyway
        # if still more than the k limit, keep increase the banana eat count
        # if already equal or less than k limit, return the current banana eat count

        # instead of brute force can use two pointer between 1 banana and max banana pile count
        # if rate more than k limit, need to increase banana eat rate, move left to mid
        # else if rate less than k limit move right to mid
        # keep going until left cross right to get the min that less than or equal k limit

        # calculate duration with current rate
        def rateToDuration(rate: int, piles: List[int]) -> int:
            duration = 0
            for pile in piles:
                duration += math.ceil(pile / rate)
            
            return duration
        
        max_pile = max(piles)
        left, right = 1, max_pile
        min_rate = max_pile
        while left < right:
            mid = left + (right - left) // 2
            
            duration = rateToDuration(mid, piles)
            if duration > h:
                # move left to mid, need to increase rate
                left = mid + 1
            else:
                # move right to mid, need to decrease rate to find min that can still satisfy, track min that satisfy
                min_rate = min(min_rate, mid)
                right = mid

        return min_rate


        