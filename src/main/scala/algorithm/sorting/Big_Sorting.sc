import scala.collection.immutable
import scala.collection.mutable.Buffer

/**
  * https://www.hackerrank.com/challenges/big-sorting/problem
  *
  * 문자열 작은 순으로 나열
  * Int.MaxValue : 2147483647 보다 큰 값
  */

val list = List(
  "6",
  "31415926535897932384626433832795",
  "1",
  "3",
  "10",
  "3",
  "5"
)

def sort(list: List[String]): List[String] =
  groupByLength(list)
    .flatMap(sortByNumber)

def groupByLength(list: List[String]): List[List[String]] =
  list.groupBy(_.size).toList
    .sortBy(_._1)
    .map(_._2)

case class Number(curNum: String, orgNum: String)

def sortByNumber(list: List[String]): List[String] =
  _sortByNumber(list.map(i => Number(i, i)))
    .map(_.orgNum)

def _sortByNumber(list: List[Number]): List[Number] = {
  if (list.size <= 1 || list.map(_.curNum).head.isEmpty) list
  else {
    list.groupBy(_.curNum.headOption.fold(-1)(_.toInt)).toList
      .filter(_._1 != -1)
      .sortBy(_._1)
      .flatMap { l =>
        _sortByNumber(l._2.map(i => i.copy(curNum = i.curNum.tail)))
      }
  }
}

sort(list)