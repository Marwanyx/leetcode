from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        prev_time = 0

        for i in range(len(logs)):
            fid, action, time = logs[i].split(":")
            fid = int(fid)
            time = int(time)
            
            if action == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time

            elif action == "end":
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res
    

s = Solution()
print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])) # [3, 4]