class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sol = []
        people.sort(key = lambda x : (-x[0],x[1]))
        # print(people)
        for person in people :
            sol.insert(person[1],person)
        return sol
        
        