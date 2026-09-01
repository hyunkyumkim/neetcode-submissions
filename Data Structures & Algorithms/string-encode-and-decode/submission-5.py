class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for s in strs:
            temp.append(str(len(s)))
            temp.append('#')
            temp.append(s)
        return "".join(temp)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            output.append(s[i:j])
            i = j
        return output