package pattern;

import com.sun.tools.javac.util.Pair;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class InsertInterval {

    public static List<Pair<Integer, Integer>> insert(int[][] list, int[] insertItem) {
        return insert(
                Arrays.stream(list).map(i -> Pair.of(i[0], i[1]))
                        .collect(Collectors.toList()),
                Pair.of(insertItem[0], insertItem[1]));
    }

    private static List<Pair<Integer, Integer>> insert(List<Pair<Integer, Integer>> list, Pair<Integer, Integer> insertItem) {
        List<Pair<Integer, Integer>> result = new ArrayList<>();
        Pair<Integer, Integer> cur = null;

        for (Pair<Integer, Integer> item : list) {
            if (isOverlapped(cur, insertItem)) {
                cur = Pair.of(Math.min(cur.fst, insertItem.fst), Math.max(cur.snd, insertItem.snd));
            } else {
                if (cur != null) {
                    result.add(cur);
                }
                cur = item;
            }
        }
        result.add(cur);
        return result;
    }

    private static boolean isOverlapped(Pair<Integer, Integer> cur, Pair<Integer, Integer> item) {
        return cur != null && cur.snd >= item.fst;
    }

    public static void main(String[] args) {
        System.out.println(insert(
                new int[][]{{ 1,3 }, { 5, 7 }, { 8, 12 }},
                new int[]{ 4, 10 }
        ));
    }
}
