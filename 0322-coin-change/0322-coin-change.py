class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)
        amounts_set = {amount}
        q = deque()
        q.append(amount)
        q_round_len = 1
        res = 0
        
        while(len(q) > 0):
            curr_list = []
            while q_round_len > 0:
                curr_list.append(q.popleft())
                q_round_len -= 1
            res += 1
            for curr in curr_list:
                for coin in coins:
                    new_val = curr - coin
                    if new_val == 0:
                        return res
                    if new_val > 0 and new_val not in amounts_set:
                        q.append(new_val)
                        amounts_set.add(new_val)
                        q_round_len += 1
 
        return -1