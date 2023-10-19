#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def count(i):
            dq, ret = [i], [i]
            while len(dq) > 0:
                # print(dq)
                i = dq.pop()
                # print(i)
                # print(adj[i])
                for j in adj[i]:
                    if j not in ret and j not in dq:
                        dq.append(j)
                        ret.append(j)
                # print(ret)
                # print('this is over')
            return len(ret)
        
        # for each bomb find the bombs can be detonated
        adj = collections.defaultdict(list)  
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                    adj[i].append(j)
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[j][2] ** 2:
                    adj[j].append(i)

        ret = 0
        for i in range(len(bombs)):
            ret = max(ret, count(i))
        return ret
# @lc code=end

