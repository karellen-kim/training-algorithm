
class MaxLongeastSequenceSolution(object):
    def findNumberOfLIS(self, nums):
        length = len(nums)
        counts = [1 for i in range(length)]

        for end in range(length) :
            for start in range(end) :
                if nums[start] < nums[end] and counts[end] <= counts[start]:
                    counts[end] = counts[start] + 1
        return max(counts)

solution = MaxLongeastSequenceSolution()
print(solution.findNumberOfLIS([1,3,5,4,7]))
print(solution.findNumberOfLIS([6, 1, 2, 8, 10, 12, 1]))
print(solution.findNumberOfLIS([1,2,4,3,5,4,7,2]))

class MaxCountLongeastSequenceSolution(object):
    def findNumberOfLIS(self, nums):
        length = len(nums)
        counts = [ [1,1] for i in range(length)]

        for end in range(length) :
            for start in range(end) :
                if nums[start] < nums[end] :
                    nextCount = counts[start][0] + 1

                    if counts[end][0] == nextCount :
                        # 값이 같으면 중복을 표기
                        counts[end] = [nextCount, counts[start][1] + counts[end][1]]
                    elif counts[end][0] <= counts[start][0] :
                        # 값이 다르면 원래대로
                        counts[end] = [nextCount, counts[start][1]]
        summary = {}
        for count in counts :
            if count[0] in summary.keys() :
                summary[count[0]] = summary[count[0]] + count[1]
            else :
                summary[count[0]] = count[1]

        if len(summary.keys()) == 0 :
            return 0
        else :
            return summary.get(max(summary.keys()))


solution = MaxCountLongeastSequenceSolution()
print(solution.findNumberOfLIS([1,3,5,4,7]))
print(solution.findNumberOfLIS([2,2,2,2,2]))
print(solution.findNumberOfLIS([6, 1, 2, 8, 10, 12, 1]))
print(solution.findNumberOfLIS([]))
print(solution.findNumberOfLIS([1,2,4,3,5,4,7,2]))
print(solution.findNumberOfLIS([1,2,3,1,2,3]))
print(solution.findNumberOfLIS([1,2,3,1,2,3,1,2,3]))
