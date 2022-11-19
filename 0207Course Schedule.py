def canFinish5(numCourses: int, prerequisites) -> bool:
        req = {i:[] for i in range(numCourses)}
        complete = []
        search = []
        for i in prerequisites:
            req[i[0]].append(i[1])
        for j in range(numCourses):
            if req[j] == []:
                complete.append(j)
        def trace(c):
            if req[numCourses] == []:
                return True
            else:
                for p in hashMap[course]:
                    if not trace(p):
                        return False       
            hashMap[course] = []
            return True 
        for c in range(numCourses):
            if not trace(c):
                return False
        return True



def canFinish4(self, numCourses: int, prerequisites) -> bool:
        prerequisites.sort(key=lambda x: x[0])
        req = []
        complete = []
        search = []
        for i in prerequisites:
            if i[0] not in req:
                req.append(i[0])
        for j in range(numCourses):
            if j not in req:
                complete.append(j)
        if complete == []:
            return False
        elif len(complete) == numCourses:
            return True
        for k in complete:
            for i in prerequisites:
                if k == i[1] and i[0] not in complete:
                    complete.append(i[0])   
        if len(complete) == numCourses:
            return True
        else:
            return False
        
        
def canFinish(numCourses: int, prerequisites) -> bool:
        hashMap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            hashMap[c].append(p)        
        visited = set()        
        def trace(course):
            print(course, hashMap, visited)
            if course in visited:
                return False
            if hashMap[course] == []:
                return True            
            visited.add(course)
            for p in hashMap[course]:
                if not trace(p):
                    return False            
            visited.remove(course)
            hashMap[course] = []
            return True        
        for c in range(numCourses):
            if not trace(c):
                return False
        return True


print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
print(canFinish(3, [[1,0],[1,2],[0,1]]))