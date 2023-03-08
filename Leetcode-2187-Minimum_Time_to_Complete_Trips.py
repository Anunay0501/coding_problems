class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        maxt=max(time)
        lo,hi=min(time), (totalTrips//sum([maxt//e for e in time]) + 1)*maxt    # I set hi earlier to 10**14, can also be set to min(time)*totalTrips.
        while lo<hi:
            m=lo+(hi-lo)//2
            trips=sum(m//ti for ti in time)
            if trips>=totalTrips:
                hi=m
            else:
                lo=m+1
        return lo