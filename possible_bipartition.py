class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        bad_people = dict()
        rooms_hotel = {}
        guest_names = []
        for tupl in dislikes:
            if tupl[0] not in bad_people:
                bad_people[tupl[0]] = [tupl[1]]
            else:
                bad_people[tupl[0]].append(tupl[1])
            if tupl[1] not in bad_people:
                bad_people[tupl[1]] = [tupl[0]]
            else:
                bad_people[tupl[1]].append(tupl[0])
        for i in range(1,N+1):
            if i not in rooms_hotel:
                rooms_hotel[i] = 0
                guest_names.append(i)
                while guest_names :
                    guest = guest_names.pop()
                    if guest in bad_people:
                        for hated in bad_people[guest]:
                            if hated in rooms_hotel:
                                if rooms_hotel[hated] == rooms_hotel[guest]:
                                    return False
                            else:
                                rooms_hotel[hated] = 1 - rooms_hotel[guest] 
                                guest_names.append(hated)
        return True
                
                
                
                
                
        
            
                