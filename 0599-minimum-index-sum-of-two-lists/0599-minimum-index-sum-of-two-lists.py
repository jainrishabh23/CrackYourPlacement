class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        r = []
        m = len(list1) + len(list2)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    s = i + j
                    if s < m:
                        r.clear()
                        r.append(list1[i])
                        m = s
                    elif s == m:
                        r.append(list1[i])
        return r
