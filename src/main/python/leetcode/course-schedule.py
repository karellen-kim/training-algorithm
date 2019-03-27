import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda course: course[1])

        time = 0
        takenCourses = []
        for course in courses :
            if time + course[0] <= course[1] :
                time += course[0]
                heapq.heappush(takenCourses, course[0] * -1)
            elif len(takenCourses) > 0 and course[0] < (takenCourses[0] * -1) :
                time = time + course[0] - (takenCourses[0] * -1)
                heapq.heappop(takenCourses)
                heapq.heappush(takenCourses, course[0] * -1)

        return len(takenCourses)


solution = Solution()
assert solution.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
