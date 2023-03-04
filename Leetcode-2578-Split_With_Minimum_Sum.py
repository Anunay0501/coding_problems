import collections


class Solution:
    def splitNum(self, num: int) -> int:
        dic=collections.Counter(str(num))
        num1,num2='',''
        for dig in sorted(dic):
            if dic[dig]%2==0:
                num1+=dig*(dic[dig]//2)
                num2+=dig*(dic[dig]//2)
            else:
                if len(num1)<=len(num2):
                    num1+=dig*((dic[dig]//2)+1)
                    num2+=dig*(dic[dig]//2)
                else:
                    num2+=dig*((dic[dig]//2)+1)
                    num1+=dig*(dic[dig]//2)
        return int(num1)+int(num2)