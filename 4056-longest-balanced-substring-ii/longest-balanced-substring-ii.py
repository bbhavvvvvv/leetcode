class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0

        pre = {(0,0): -1}
        run_ab,run_ac = 0,0

        for i in range(len(s)):
            if s[i] == "a":
                run_ab += 1
                run_ac += 1
            elif s[i] == "b":
                run_ab -= 1
            else:
                run_ac -= 1
            key = (run_ab,run_ac)

            if key in pre:
                res = max(res, i - pre[key])
            else:
                pre[key] = i

        def solveXY(x,y):
            pre_sum ={0:-1}
            run_sum = 0
            ans = 0
            for i in range(len(s)):
                if s[i] == x:
                    run_sum += 1
                elif s[i] == y:
                    run_sum -= 1
                else:
                    pre_sum = {0:i}
                    run_sum = 0
                if run_sum in pre_sum:
                    ans = max(ans,i-pre_sum[run_sum])
                else:
                    pre_sum[run_sum] = i
            return ans

        res = max(res,solveXY("a","b"),solveXY("a","c"),solveXY("c","b"))

        def solveX(x):
            ans = 0
            count = 0
            for char in s:
                if char != x:
                    count = 0
                else:
                    count += 1
                    ans = max(ans, count)
            return ans

        res = max(res,solveX("a"), solveX("b"), solveX("c"))
        return res
            
      