class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # TC: O(n*m)

        if len(s1) > len(s2):
            return False

        counter = Counter(s1)
        n = len(s1)

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
            # since (i-n) letter in not within curr window, increment it
            if i>=n and s2[i-n] in counter:
                counter[s2[i-n]] += 1

            charCount = True
            for ch in counter:
                if counter[ch] != 0:
                    charCount = False
                    break
            if charCount: return True
        return False

