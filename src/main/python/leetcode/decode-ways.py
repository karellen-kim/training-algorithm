class Solution:
    def numDecodings(self, s: str) -> int:
        splitIndexes = []
        self.split(range(len(s) - 1), [], splitIndexes, len(s) - 1)

        count = 0
        for splitIndex in splitIndexes :
            preIndex = 0
            encodable = True
            for index in splitIndex :
                encodedChar = s[preIndex:index]
                if self.encodableChars(encodedChar) == False :
                    encodable = False
                    break;
                preIndex = index
            if encodable :
                count += 1

        return count

    def encodableChars(self, char):
        return char.startswith('0') == False and int(char) >= 1 and int(char) <= 26

    def split(self, indexes, list, splitIndexes, lastIndex):
        if len(indexes) == 0 :
            splitIndexes.append(self.append(list, lastIndex + 1))
        else :
            self.split(indexes[1:], list, splitIndexes, lastIndex)
            self.split(indexes[1:], self.append(list, indexes[0] + 1), splitIndexes, lastIndex)

    def append(self, list, item):
        new_list = list[:]
        new_list.append(item)
        return new_list

solution = Solution()
#print(solution.numDecodings("12"))
#print(solution.numDecodings("226"))
#print(solution.numDecodings("01"))
print(solution.numDecodings("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"))
