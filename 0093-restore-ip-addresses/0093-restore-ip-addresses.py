class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(curr, remS):
            nonlocal res

            if len(curr) == 4 and not remS:
                res.append('.'.join(curr))
            if len(curr) == 4 or not remS:
                return
            
            for i in range(3):
                if len(remS) > i:
                    newS, newRemS = remS[0: i + 1], remS[i + 1:]
                    if len(newS) > 1 and newS[0] == '0':
                        break
                    if int(newS) > 255 or int(newS) < 0:
                        break
                    curr.append(newS)
                    backtrack(curr, newRemS)
                    curr.pop()
              
        backtrack([], s)
        return res
