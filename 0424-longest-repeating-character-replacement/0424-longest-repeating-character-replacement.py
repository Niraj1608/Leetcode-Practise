class Solution:
   
    def characterReplacement(self, s: str, k: int) -> int:
        alphabets = {}

        ans = 0
        left = 0
        right = 0

        for right in range(len(s)) :
            alphabets[s[right]] = 1 + alphabets.get(s[right] , 0)

            if (right - left + 1) - max(alphabets.values()) > k :
                alphabets[s[left]] -= 1
                left += 1
            else :
                ans = max(ans , (right - left + 1) )   

        return ans         


        

        