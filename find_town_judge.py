class Solution(object):
    def findJudge(self, N, trust):
        if len(trust) < N-1:
            return False
        trust_map = dict()
        for i in range(1, N+1):
            trust_map[i] = []
        for trustee in trust:
            trust_map[trustee[0]].append(trustee[1])
        for key, value in trust_map.items():
            if trust_map[key] == []:
                if self.search_key(key, trust_map):
                    return key
                return -1
        return -1

    def search_key(self, key, trust_map):
        for keyy, item in trust_map.items():
            if key not in item and key != keyy:
                return False
        return True
