class Logger:

    def __init__(self):
        self.messageMap = {};

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messageMap and self.messageMap[message] + 10 > timestamp:
            return False
            
        self.messageMap[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)