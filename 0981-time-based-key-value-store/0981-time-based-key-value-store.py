class TimeMap:

    def __init__(self):
        self.tdict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tdict:
            self.tdict[key] = []
        self.tdict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.tdict.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r)//2
            
            if values[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
                res = values[m][0]
                if values[m][1] == timestamp:
                    break
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)