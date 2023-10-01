class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        lst = {}
        opt = ""
        for i in range(numRows):
            lst[f'{i}'] = []

        k = 0
        zigzag = numRows - 2
        for i in range(len(s)):
            if (k != numRows):
                lst[f"{k}"].append(s[i])
                k += 1
                zigzag = numRows - 2
            else:
                lst[f"{zigzag}"].append(s[i])
                zigzag -= 1
                if zigzag <= 0:
                    k = 0
                if numRows == 2:
                    k = 1

        for row, val in lst.items():
            opt += "".join(val)

        return opt
            

