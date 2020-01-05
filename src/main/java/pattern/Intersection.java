package pattern;

import com.sun.tools.javac.util.Pair;

import javax.lang.model.type.IntersectionType;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author karellen
 */
public class Intersection {

    public static List<Pair<Integer, Integer>> intersection(List<Pair<Integer, Integer>> list1,
                                                            List<Pair<Integer, Integer>> list2) {
        List<Pair<Integer, Integer>> result = new ArrayList<>();
        int idx1 = 0;
        int idx2 = 0;

        while (idx1 < list1.size() && idx2 < list2.size()) {
            Pair<Integer, Integer> item1 = list1.get(idx1);
            Pair<Integer, Integer> item2 = list2.get(idx2);

            if (overlaped(item1, item2)) {
                result.add(Pair.of(Math.max(item1.fst, item2.fst), Math.min(item1.snd, item2.snd)));
            }

            if (item1.snd < item2.snd) {
                idx1++;
            } else {
                idx2++;
            }
        }

        return result;
    }


    public static boolean overlaped(Pair<Integer, Integer> item1, Pair<Integer, Integer> item2) {
        // item1의 시작점이 item2의 가운데 있거나
        // item2의 시작점이 item1의 가운데 있다.
        return (item1.fst >= item2.fst && item1.fst <= item2.snd) ||
                (item2.fst >= item1.fst && item2.fst <= item1.snd);
    }

    private static List<Pair<Integer, Integer>> convert(int[][] list) {
        return Arrays.stream(list).map(i -> Pair.of(i[0], i[1]))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        System.out.println(intersection(
                convert(new int[][]{{1, 3}, {5, 6}, {7, 9}}),
                convert(new int[][]{{2, 3}, {5, 7}})
        ));

        System.out.println(intersection(
                convert(new int[][]{{1, 3}, {5, 7}, {9, 12}}),
                convert(new int[][]{{5, 10}})
        ));
    }
}
