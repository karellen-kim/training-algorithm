/**
  * https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
  * [3, -7, 0]
  * (3, -7) => 10, (3, 0) => 3, (-7, 0) => 7 두 원소의 최소 차이 값 3
  */
object Diff {

  implicit class OptionOps(a: Option[Int]) {
    def < (b: Option[Int]): Boolean =
      (for {
        i <- a
        j <- b
      } yield i < j).getOrElse(true)
  }

  def minimumAbsoluteDifference(arr: List[Int]): Option[Int] = {
    val sortedArray = arr.sorted
    var min: Option[Int] = None
    var prev: Option[Int] = None

    sortedArray.foreach { item =>
      val diff = prev.map(p => Math.abs(p - item))
      if (diff < min) min = diff
      prev = Some(item)
    }
    min
  }
}



Diff.minimumAbsoluteDifference(List(3,-7,0)) // 3
Diff.minimumAbsoluteDifference(List(-59, -36, -13, 1, -53, -92, -2, -96, -54, 75)) // 1