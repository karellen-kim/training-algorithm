class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        map = {}
        for word in words :
            map[word] = map.get(word, 0) + 1

        list = [0 for range(0, len(map))]
        for word in map :
            map[word]

solution = Solution()
print(solution.topKFrequent(words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2))