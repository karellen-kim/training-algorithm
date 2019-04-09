class SolutionV1:
    def numDecodings(self, s) :
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

solution = SolutionV1()
print(solution.numDecodings("12"))
print(solution.numDecodings("226"))
print(solution.numDecodings("01"))
# Time Limit Exceeded
# print(solution.numDecodings("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"))


class SolutionV2:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]

solution = SolutionV2()
print(solution.numDecodings("12"))
print(solution.numDecodings("226"))
print(solution.numDecodings("01"))
print(solution.numDecodings("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"))
print(solution.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))