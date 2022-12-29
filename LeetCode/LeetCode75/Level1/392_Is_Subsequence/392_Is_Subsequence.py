class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        count = 0
        target = len(s)
        len_t = len(t)

        if not s:
            return True

        if target > len_t:
            return False

        if target == len_t:
            if s == t:
                return True
            else:
                return False

        for t_index, t_char in enumerate(t):
            s_char = s[s_index]
            if s_char == t_char:
                count += 1
                s_index += 1
            if count == target:
                return True
        return False



if __name__ == "__main__":
    sol = Solution()
    testcases = [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc")
    ]

    for t_case_num, t_case_ip in enumerate(testcases):
        s = t_case_ip[0]
        t = t_case_ip[1]
        r = sol.isSubsequence(s, t)
        print(f"Test Case Number: {t_case_num}")
        print(f"Inputs:\ns={s}\tt={t}\n")
        print(f"Output: {r}\n")
        print("#"*30)
        print("\n")




