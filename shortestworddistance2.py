from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.mapping = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.mapping[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        mapping = self.mapping

        if len(mapping[word1]) == 1 and len(mapping[word2]) == 1:
            return abs(mapping[word1][0] - mapping[word2][0])
        
        list1 = mapping[word1]
        list2 = mapping[word2]

        res = 10000000

        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            res = min(res, abs(list1[i] - list2[j]))

            if i == len(list1) - 1:
                j += 1
                continue
            
            if j == len(list2) - 1:
                i += 1
                continue
            
            if list1[i] < list2[j]:
                i += 1
                continue
            else:
                j += 1
                continue


        return res



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# practice makes perfect coding makes
# practice -> [0]
# makes -> [1, 4]
# perfect -> [2]
# coding -> [3]

# [5, 7 ,8, 9]
# [0, 100, 101]

# The reason why this works is we're using the property that when building this word -> List of indices hashmap,
# the list of indices of occurrence for every word is sorted inherently.
# we can then use this "greedy" formulation of finding the smallest pair difference between 2 sorted lists
# which relies on the fact that we should advance the smaller number first. Why? because advancing the larger number will only make 
# the current difference larger.
