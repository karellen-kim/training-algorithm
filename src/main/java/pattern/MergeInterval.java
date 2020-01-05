package pattern;

import com.sun.tools.javac.util.Pair;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/**
 * @author karellen
 */
public class MergeInterval {

    public static List<Pair<Integer, Integer>> merge(List<Pair<Integer, Integer>> intervals) {
        intervals.sort(Comparator.comparing(pair -> pair.fst));

        List<Pair<Integer, Integer>> result = new ArrayList<>();

        Pair<Integer, Integer> prev = null;
        for (Pair<Integer, Integer> item : intervals) {
            if (overlaped(prev, item)) {
                prev = Pair.of(prev.fst, Math.max(prev.snd, item.snd));
            } else {
                if (prev != null) {
                    result.add(prev);
                }
                prev = item;
            }
        }
        result.add(prev);
        return result;
    }

    private static boolean overlaped(Pair<Integer, Integer> prev, Pair<Integer, Integer> cur) {
        return prev != null && prev.snd >= cur.fst;
    }

    public static void main(String[] args) {
        System.out.println(merge(
                Arrays.asList(
                        Pair.of(1, 4), Pair.of(2, 5), Pair.of(7, 9)
                )
        ));

        System.out.println(merge(
                Arrays.asList(
                        Pair.of(6, 7), Pair.of(2, 4), Pair.of(5, 9)
                )
        ));

        System.out.println(merge(
                Arrays.asList(
                        Pair.of(1, 4), Pair.of(2, 6), Pair.of(3, 5)
                )
        ));
    }
}
