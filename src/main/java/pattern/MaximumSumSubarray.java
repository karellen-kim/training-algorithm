package pattern;

import java.util.Arrays;
import java.util.List;

public class MaximumSumSubarray {
    public static int get(List<Integer> list, int k) {

        int maximumSum = 0;
        int currentSum = 0;
        for (int i = 0 ; i < list.size() ; i++) {
            currentSum = currentSum + getOrElse(list, i, 0) - getOrElse(list, i - k, 0);
            maximumSum = Math.max(maximumSum, currentSum);
        }
        return maximumSum;
    }

    public static int getOrElse(List<Integer> list, int index, int defaultValue) {
        if (index < list.size() && index >= 0) {
            return list.get(index);
        } else {
            return defaultValue;
        }
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(2,1,5,1,3,2);
        int k = 3;
        System.out.println(MaximumSumSubarray.get(list, k));
    }
}
