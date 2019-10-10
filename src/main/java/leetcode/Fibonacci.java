package leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * @author karellen
 */
public class Fibonacci {

    Map<Integer, Integer> memorization = new HashMap<>();

    public int get(int idx) {
        if (idx <= 1) return idx;

        if (memorization.containsKey(idx)) {
            return memorization.get(idx);
        } else {
            int value = get(idx - 1) + get(idx - 2);
            memorization.put(idx, value);
            return value;
        }
    }

    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();
        System.out.println(fibonacci.get(4));
        System.out.println(fibonacci.get(6));
    }
}
