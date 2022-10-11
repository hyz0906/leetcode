from string import ascii_lowercase

class Solution:
    def robotWithString(self, s: str) -> str:
        p = []
        s_len = {}
        for item in s:
            if item not in s_len.keys():
                s_len[item] = 1
            else:
                s_len[item] += 1
        print(s_len)
        min_char = 0
        t = []
        for char in s:
            print("**")
            print(char)
            print(s_len[char])
            s_len[char] -= 1

            while min_char < len(ascii_lowercase)-1 and s_len.get(ascii_lowercase[min_char],0) == 0:
                min_char += 1
                print("***")
                print(s_len.get(ascii_lowercase[min_char],0), min_char)
            t.append(char)
            print("****")
            print(t)
            while t and t[-1] <= ascii_lowercase[min_char]:
                p.append(t.pop())
                print(min_char, p)
                print(t)
        return ''.join(p)


def main():
    sol = Solution()

    print(sol.robotWithString('bdbde'))


if __name__ == main():
    main()
