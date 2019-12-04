
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs) :
        # O(N)
        list = [i for i in range(len(s))]

        # O(M)
        for pair in pairs :
            tmp = list[pair[0]]
            list[pair[0]] = list[pair[1]]
            list[pair[1]] = tmp

        # O(N)
        swapedString = []
        for idx in list :
            swapedString.append(s[idx])
        print(list)
        return "".join(swapedString)

solution = Solution()
print(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))
print(solution.smallestStringWithSwaps("dcab", [[0, 3], [0, 2], [1, 2]]))
print(solution.smallestStringWithSwaps("cba", [[0,1], [1,2], [0,1]]))
