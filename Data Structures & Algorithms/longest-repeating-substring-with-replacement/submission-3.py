class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #sliding window + hashmap

        window = defaultdict(int)
        l = 0

        maxlength = 0
        for r in range(len(s)):
            
            window[s[r]] += 1

            if ((r - l)+1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            
            maxlength = max(maxlength, (r - l) + 1)
        
        return maxlength


                
            

