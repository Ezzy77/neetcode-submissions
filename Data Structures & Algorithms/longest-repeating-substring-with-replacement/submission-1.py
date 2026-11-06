class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            # update frequency of current char
            count[char] = count.get(char, 0) + 1
            # track highest freq 
            max_freq = max(max_freq, count[char])

            # check if the window is valid
            window_length = right - left + 1
            if window_length - max_freq > k:
                # shrink the window from left
                count[s[left]] -= 1
                left += 1
            # update the longest valid window
            max_length = max(max_length, right - left + 1)
        return max_length

        