/**
  * https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
  */

val list = List(1, 3, 2, 6, 1, 2)
val divisibleNumber = 3

def findPairs(list: List[Int]): List[(Int, Int)] = {
  list match {
    // 2개 이상일때
    case head :: second :: tail =>
      val pairs = list.tail.toList.map(n => (head, n))
      pairs ::: findPairs(list.tail)
    // 2개 미만일때 => 결과 없음
    case _ => Nil: List[(Int, Int)]
  }
}

findPairs(list)
  .filter(pairs => (pairs._1 + pairs._2) % divisibleNumber == 0)
  .size