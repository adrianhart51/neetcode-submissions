class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input validation
        if len(s) <= 1:
            return True
        
        # set two pointer at start and end of string -> left, right
        # check if left alphanumeric, if not move right
        # check if right alphanumeric, if not move left
        # check until left and right overlap
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1

            # because left and right always move until find alphanumeric
            # if left and right alphanumeric but different char return false
            # if until overlap always same alphanumeric, when finish iterate return true
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


        # simulate
        # "was a saw?"
        #     rl -> True

        # "tab a cat"
        #    l   r -> False
