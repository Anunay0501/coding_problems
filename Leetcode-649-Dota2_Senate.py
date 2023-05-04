from collections import Counter, deque


class Solution:
    
    def predictPartyVictory(self, senate: str) -> str:
        frq = Counter(senate)
        q = deque([ltr for ltr in senate])
        dump = {'R': 0, 'D': 0}
        
        while frq['R'] != 0 and frq['D'] != 0:
            ch = q.popleft()
            if dump[ch] > 0:
                frq[ch] -= 1
                dump[ch] -= 1

            else:
                q.append(ch)
                if ch == 'R':
                    dump['D'] += 1
                else:
                    dump['R'] += 1
        
        
        return 'Dire' if frq['R'] == 0 else 'Radiant'