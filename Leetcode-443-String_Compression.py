class Solution:
    def compress(self, chars) -> int:
        # write pointer to enter the shortened span, left to remember the letter whose window we are looking for.
        write = left = 0
        for right, ch in enumerate(chars):

            if ch != chars[left]:
                if right-left > 1:
                    for c in chars[left]+str(right-left):
                        chars[write] = c
                        write += 1
                else:
                    chars[write] = chars[left]
                    write += 1
                left = right
        
        # You have to also count the last span since it wasn't added.
        right += 1
        
        if right-left > 1:
            for c in chars[left]+str(right-left):
                chars[write] = c
                write += 1
        else:
            chars[write] = chars[left]
            write += 1

        return write