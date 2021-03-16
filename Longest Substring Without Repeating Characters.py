class Solution:
           
    def lengthOfLongestSubstring(self, s: str) -> int:
        
                
        last_idx = {}
        count = 0

        start_idx = 0

        for i in range(0, len(s)):

            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1)
           
            count = max(count, i-start_idx + 1)

            last_idx[s[i]] = i
            
           
        
                    
                
        return count   