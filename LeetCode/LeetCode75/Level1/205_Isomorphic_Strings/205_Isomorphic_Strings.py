from typing import Dict


class Solution:
    def count_char_occurences(self, s: str) -> Dict:
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        return counter

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_count = self.count_char_occurences(s)
        t_count = self.count_char_occurences(t)
        if len(s_count.keys()) != len(t_count.keys()):
            return False

        char_map = {}
        for index, s_char in enumerate(s):
            t_char = t[index]
            if s_char in char_map:
                test_char = char_map[s_char]
                if test_char != t_char:
                    return False
            else:
                char_map[s_char] = t_char
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "foo"
    t = "bar"
    result = sol.isIsomorphic(s, t)
    print(result)
