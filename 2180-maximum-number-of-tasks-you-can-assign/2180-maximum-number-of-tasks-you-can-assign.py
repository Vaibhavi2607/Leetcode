class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse = True)
        def can_used(k : int) -> bool:
            cnt = 0
            p = pills
            q = deque[int]()
            for i in range(k - 1, -1, -1):
                if len(q) == 0 and workers[cnt] >= tasks[i]:
                    cnt += 1
                    continue
                if len(q) > 0 and q[0] >= tasks[i]:
                    q.popleft()
                    continue
                while cnt < k and workers[cnt] + strength >= tasks[i]:
                    q.append(workers[cnt])
                    cnt += 1
                if len(q) > 0 and p > 0:
                    q.pop()
                    p -= 1
                    continue
                return False
            return True
        
        left = 0
        right = min(len(tasks), len(workers))
        used = 0
        while left <= right:
            mid = (left + right) // 2
            if can_used(mid):
                used = mid
                left = mid + 1
            else:
                right = mid - 1
        return used