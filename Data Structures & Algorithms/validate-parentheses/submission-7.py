class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in closeToOpen:
                s = s.replace("()", "")
                s = s.replace("{}", "")
                s = s.replace("[]", "")
        return s == ""
        