class Solution:
    def distMoney(self, money: int, children: int) -> int: 
        if money < children:
            return -1
        elif money == children:
            return 0
        else:
            count = 0
            money -= children
            for i in range(children):
                if money >= 7:
                    count += 1
                    money -= 7
                elif money == 3:
                    if i == children-1:
                        return count-1 if count > 0 else 0
                    else:
                        return count
                else:
                    return count
            if not money:
                return count
            else:
                return count-1
