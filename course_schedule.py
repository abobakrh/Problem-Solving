class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_zero = []
        removed = 0
        in_deg = collections.defaultdict(set)
        out_deg = collections.defaultdict(set)
        for course,preq in prerequisites:
            in_deg[course].add(preq)
            out_deg[preq].add(course)
        for i in range(numCourses):
            if not in_deg[i]:
                in_zero.append(i)
                removed += 1
        while in_zero:
            c = in_zero.pop()
            for neighbor in out_deg[c]:
                in_deg[neighbor].remove(c)
                if not in_deg[neighbor]:
                    in_zero.append(neighbor)
                    removed += 1
        return removed == numCourses
                
        
        
        
            
            
        