import scala.collection.mutable.Buffer

/**
  * https://www.hackerrank.com/challenges/reduced-string/problem
  * 인접한 두쌍의 문자열이 동일한 경우 삭제한다
  * baabccc -> bbccc -> ccc -> c
  */
def reduceStrings(chars: String): String = {
  val reduced = reduceStringsImpl(chars.toCharArray.toList).mkString

  if (reduced.isEmpty) "Empty String"
  else reduced
}

def reduceStringsImpl(chars: List[Char]): List[Char] = {
  (0 until chars.size - 1)
    .dropWhile { i => chars(i) != chars(i + 1) }
    .headOption
    .fold(chars) { i =>
      reduceStringsImpl(removeSameChars(chars, i, i + 1))
    }
}

def removeSameChars(chars: List[Char], from: Int, to: Int): List[Char] = {
  val list = Buffer.empty[Char]

  list.appendAll(chars.take(from))
  list.appendAll(chars.drop(to + 1))
  list.toList
}

reduceStrings("aaabccddd") // abd
reduceStrings("aa") // Empty String
reduceStrings("baab") // Empty String