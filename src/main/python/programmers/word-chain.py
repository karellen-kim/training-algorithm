import math

def solution(n, words):

    if len(words) > 0:
        usedWord = set()
        lastChar = words[0][0]
        for idx, word in enumerate(words) :
            if word in usedWord or word[0] != lastChar:
                return [idx % n + 1, math.ceil(float(idx + 1) / n)]
            else :
                lastChar = word[-1]
                usedWord.add(word)

    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
