class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])  # reuse allowed
                path.pop()

        backtrack(0, [], target)
        return res
