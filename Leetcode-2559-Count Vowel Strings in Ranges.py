class Solution:
    def vowelStrings(self, words, queries):
        
        vow = {'a', 'e', 'i', 'o', 'u'}
        arr = [0]

        #
        for word in words:
            if word[0] in vow and word[-1] in vow:
                arr.append(arr[-1]+1)
            else:
                arr.append(arr[-1])
        

        return [arr[i2+1]-arr[i1] for i1, i2 in queries]
