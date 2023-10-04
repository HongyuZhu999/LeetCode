#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ready = [r for r in range(n)]
        rooms = []
        heapify(ready)
        res = [0] * n
        print(ready)
        
        for s, e in sorted(meetings):
            while rooms and rooms[0][0] <= s:
                t, r = heappop(rooms)
                heappush(ready, r)
            if ready:
                r = heappop(ready)
                heappush(rooms, [e, r])
            else:
                t, r = heappop(rooms)
                heappush(rooms, [t + e - s, r])
            res[r] += 1
        return res.index(max(res)) 

# @lc code=end

