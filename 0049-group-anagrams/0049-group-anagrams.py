class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            key = "".join(sorted(str))

            if key not in dict:
                dict[key] = []
            
            dict[key].append(str)

        return list(dict.values())