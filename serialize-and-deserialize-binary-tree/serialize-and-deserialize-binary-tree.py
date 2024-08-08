# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.append(root)
        res = []
        while q:
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                if not curr:
                    res.append('null')
                else:
                    res.append(str(curr.val))
                    q.append(curr.left)
                    q.append(curr.right)
        
        
        resString = ','.join(res)
        return resString     
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        data = data.split(',')
        q = deque()
        root = None
        if data and data[0] != 'null':
            root = TreeNode(int(data[0]))     
            q.append(root)           
        i = 1
        while q:
            curr = q.popleft()
            valLeft = data[i]
            valRight = data[i+1]
                            
            left, right = None, None
            if valLeft != 'null':
                left = TreeNode(int(valLeft))
                q.append(left)
            if valRight != 'null':
                right = TreeNode(int(valRight))
                q.append(right)
                            
            curr.left = left
            curr.right = right                
            i += 2
            
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))