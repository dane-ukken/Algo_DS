class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        resList = []
        for s in strs:
            count = len(s)
            curr = []
            # abc is the length of the string
            
            c = count%10
            count = count // 10
            b = count % 10
            count = count // 10
            a = count
            
            curr.append(str(a))
            curr.append(str(b))
            curr.append(str(c))
            curr.append(s)
            
            resList.append("".join(curr))
            
        return "".join(resList)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        resList = []
        
        while i < len(s):
            j = i+3
            l = int(s[i:j])
            curr = ""
            i = j + l
            if l != 0:
                curr = s[j:j+l]
            resList.append(curr)
        
        return resList
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))