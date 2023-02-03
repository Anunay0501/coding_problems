class Solution:
    def conversion1(self, s, numRows):
        # lets's suppose s='1234567890abcdefgh' and numRows=4,then required ans =
        #         1       7       c
        #         2     6 8     b d     h
        #         3  5    9  a    e  g
        #         4       0       f
        # ans='17c268bdh359aeg40f'

        # therefore,if k=numRows-1 and  i=ind of ch in s,then
        # 0                             2k
        # 1                     2k-1    2k+1
        # 2                 2k-2        2k+2
        # .             ..                .
        # .           ..                  .
        # .        ..                     .
        # k-1  k+1                      3k-1
        # k                             3k
        #  arr=['']*numRows
        if numRows == 1:
            return s
        arr, k = ['']*numRows, numRows-1
        for ind, ch in enumerate(s):
            div, rem = ind//k, ind % k
            if rem == 0:
                if div % 2 == 0:
                    arr[0] += ch
                else:
                    arr[-1] += ch
            else:
                if div % 2 == 0:
                    arr[rem] += ch
                else:
                    arr[-1-rem] += ch
        # This works well but this is not an O(n) solution because of arr[index]+=ch
        return ''.join(arr)

        # Two things that can be done -> (1) the oscillation from  0 and k(numRow-1) can be done better. (2) use stack instead of strings
    def conversion2(self, s, numRows):
        n = len(s)
        if numRows == 1 or n <= numRows:
            return s
        ind, step = 0, 1
        ans = [[] for ind in range(n)]
        for ch in s:
            ans[ind].append(ch)
            if ind == 0:
                step = 1
            elif ind == numRows-1:
                step = -1
            ind += step
        return ''.join([''.join(row) for row in ans])


sol = Solution()
print(sol.conversion1(s="PAYPALISHIRING", numRows=3))
print(sol.conversion2(s="PAYPALISHIRING", numRows=3))
