package pattern;

import com.sun.tools.javac.util.Pair;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author karellen
 */
public class ConflictAppointment {

    public static boolean conflict(List<Pair<Integer, Integer>> appointments) {
        List<Pair<Integer, Integer>> list =
                appointments
                        .stream()
                        .sorted(Comparator.comparing(i -> i.fst))
                        .collect(Collectors.toList());

        for (int i = 1 ; i < list.size() ; i++) {
            if (overlapped(list.get(i - 1), list.get(i))) {
                return true;
            }
        }
        return false;
    }

    public static boolean overlapped(Pair<Integer, Integer> item1, Pair<Integer, Integer> item2) {
        return item1 != null && item2.fst >= item1.fst && item2.fst <= item1.snd;
    }

    private static List<Pair<Integer, Integer>> convert(int[][] list) {
        return Arrays.stream(list).map(i -> Pair.of(i[0], i[1]))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        System.out.println(!conflict(
                convert(new int[][]{{1, 4}, {2, 5}, {7, 9}})
        ));

        System.out.println(!conflict(
                convert(new int[][]{{6, 7}, {2, 4}, {8, 12}})
        ));

        System.out.println(!conflict(
                convert(new int[][]{{4, 5}, {2, 3}, {3, 6}})
        ));
    }

}
