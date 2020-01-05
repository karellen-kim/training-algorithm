import scala.collection.mutable.Buffer

/**
  * https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
  *
  * ar = [1,2,3,5,9], k = 1
  * 원소간 차이가 k 이하인 배열로 쪼갠다 => [1,2,3], [5], [9]
  */

case class SplitList(var list: Buffer[Buffer[Int]] = Buffer(Buffer()),
                     var curIdx: Int = 0) {
  def add(item: Int): SplitList = {
    list(curIdx).append(item)
    this
  }
  def split: SplitList = {
    list.append(Buffer())
    curIdx = curIdx + 1
    this
  }
  def toList = list.map(_.toList).toList
}

def splitByRange(ar: List[Int], range: Int): List[List[Int]] = {
  val sortedArray = sort(ar.toSet.toList)

  val list = SplitList()
  var prevItem: Option[Int] = None
  sortedArray.foreach { item =>
    if (prevItem.fold(0)(v => item - v) <= range) list.add(item)
    else list.split.add(item)

    prevItem = Some(item)
  }
  list.toList
}

//def sort(ar: List[Int]) = ar.sorted

def sort(ar: List[Int]): List[Int] = {
  if (ar.size <= 1) ar
  else {
    val (first, second) = ar.splitAt(ar.size / 2)
    val sortedFirst = sort(first)
    val sortedSecond = sort(second)

    merge(sortedFirst, sortedSecond)
  }
}

def merge(sortedFirst: List[Int], sortedSecond: List[Int]): List[Int] = {
  val list = Buffer[Int]()

  var i, j = 0
  while (i < sortedFirst.size && j < sortedSecond.size) {
    if (sortedFirst(i) < sortedSecond(j)) {
      list.append(sortedFirst(i))
      i = i + 1
    } else {
      list.append(sortedSecond(j))
      j = j + 1
    }
  }
  sortedFirst.splitAt(i)._2.foreach(item => list.append(item))
  sortedSecond.splitAt(j)._2.foreach(item => list.append(item))

  list.toList
}

def hackerlandRadioTransmitters(ar: List[Int], range: Int): Int =
  splitByRange(ar, range)
    .map { list =>
      val rangeCount = if (list.size > 1) list.size - 1 else list.size
      Math.ceil(rangeCount.toDouble/(range + 1)).toInt
    }.sum

splitByRange(List(), 1)
splitByRange(List(1,2,3,5,9), 1)
splitByRange(List(1,2,3,5,9), 2)
splitByRange(List(2,2,2,2,1,1,1,1), 2)

hackerlandRadioTransmitters(List(), 1)
hackerlandRadioTransmitters(List(1,2,3,5,9), 1)
hackerlandRadioTransmitters(List(1,2,3,5,9), 2)
hackerlandRadioTransmitters(List(2,2,2,2,1,1,1,1), 2)