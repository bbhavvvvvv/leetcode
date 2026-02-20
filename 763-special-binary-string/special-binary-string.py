class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s :
            return ""
        results = []
        count = 0
        i = 0

        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                inner_part = self.makeLargestSpecial(s[i+1:j])
                results.append(f"1{inner_part}0")
                i = j+1
        results.sort(reverse=True)

        return "".join(results)
        