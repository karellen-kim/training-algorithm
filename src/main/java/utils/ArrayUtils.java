package utils;

import com.sun.tools.javac.util.Pair;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ArrayUtils {
    public static List<Pair<Integer, Integer>> convertToPair(int[][] arr) {
        return Arrays.stream(arr).map(i -> Pair.of(i[0], i[1]))
                .collect(Collectors.toList());
    }
}
