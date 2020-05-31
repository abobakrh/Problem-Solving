class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {}
        ans = ""
        s_nodups = "".join(set(s))
        for char in s_nodups :
            my_dict[char] = s.count(char)
        my_dict = collections.OrderedDict(sorted(my_dict.items(), key = lambda kv:(kv[1], kv[0])))
        for char,freq in my_dict.items():
            for _ in range(freq):
                ans += char
        return ''.join(reversed(ans))
            
            
        