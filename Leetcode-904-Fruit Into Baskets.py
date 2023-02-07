class Solution:
    def totalFruit(self, fruits) -> int:
        #Initiate a sliding window,storing frequency of each fruit and maintaining the hashmap of length 2. Return the maximum window.
        left = ans = 0
        dic = {}

        for right, fruit in enumerate(fruits):
            if fruit in dic:
                dic[fruit] += 1
            else:
                dic[fruit] = 1

            while len(dic) > 2:
                dic[fruits[left]] -= 1

                if dic[fruits[left]] == 0:
                    dic.pop(fruits[left])
                left += 1

            ans = max(ans, right-left+1)


        return ans