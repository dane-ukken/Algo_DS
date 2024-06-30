class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys = set({0})
        
        def dfs(room):
            if room not in keys: 
                return
            if room in visited:
                return
            keys.update(rooms[room])
            visited.add(room)
            for nextRoom in rooms[room]:
                dfs(nextRoom)
        
        dfs(0)
        return True if len(visited) == len(rooms) else False