class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            while "()" in s or "[]" in s or "{}" in s:
                s = s.replace("()", "")
                s = s.replace("{}", "")
                s = s.replace("[]", "")
        return s == ""
        