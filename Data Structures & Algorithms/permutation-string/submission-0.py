class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        # check first window
        if count1 == count2:
            return True
        
        # Slide the window across s2
        for right in range(len(s1), len(s2)):
            # Add the new character
            count2[ord(s2[right]) - ord('a')] += 1

            # Remove the character leaving the window
            left = right - len(s1)
            count2[ord(s2[left]) - ord('a')] -= 1

            # Check whether the frequencies match
            if count1 == count2:
                return True

        return False


        