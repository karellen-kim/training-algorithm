package pattern;

import java.util.Arrays;
import java.util.List;

/**
 * @author karellen
 */
public class SmallestSubarray {

    static class Pos {
        public int start;
        public int end;
        Pos(int start, int end) {
            this.start = start;
            this.end = end;
        }
        public int getLength() {
            return this.end - this.start + 1;
        }
    }

    public static int get(List<Integer> list, int sum) {
        Pos smallestPos = new Pos(0, Integer.MAX_VALUE - 1);
        Pos currentPos = new Pos(0, 0);

        int currentSum = 0;
        for (int i = 0 ; i < list.size() ; i++) {
            currentPos.end = i;
            currentSum += list.get(i);

            while (currentSum >= sum) {
                if (smallestPos.getLength() > currentPos.getLength()) {
                    smallestPos = currentPos;
                }
                currentSum -= list.get(currentPos.start);
                currentPos.start += 1;
            }
        }
        return smallestPos.getLength();
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(2, 1, 5, 2, 3, 2);
        int sum = 7;

        System.out.println(SmallestSubarray.get(list, sum));
    }
}
