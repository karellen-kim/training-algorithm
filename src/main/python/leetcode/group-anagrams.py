class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for str in strs :
            key = self.getKey(str)
            if map.get(key) == None :
                map[key] = []

            anagrams = map.get(key, [])
            anagrams.append(str)

        return map.values()

    def getKey(self, chars):
        list = [0 for idx in range(ord('z') - ord('a') + 1)]
        for ch in chars :
            idx = ord(ch) - ord('a')
            list[idx] = list[idx] + 1

        return "".join([str(ch) for ch in list])

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha", "nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))
print(solution.groupAnagrams(["tin","ram","zip","cry","pus","jon","zip","pyx"]))
