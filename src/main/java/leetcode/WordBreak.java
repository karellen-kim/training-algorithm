package leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * @author karellen
 */
public class WordBreak {

    /**
     * Time Limit Exceeded Solution
     */
    public static boolean wordBreak(String str, Set<String> dict) {
        if (str.length() == 0) {
            return true;
        }

        for (int i = 0; i <= str.length() ; i++) {
            String word = str.substring(0, i);
            if (dict.contains(word)) {
                if (wordBreak(str.substring(i), dict)) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Non-Recursion Solution
     */
    public static boolean wordBreakII(String str, Set<String> dict) {
        boolean[] checked = new boolean[str.length() + 1];

        checked[0] = true;
        for (int i = 1 ; i < str.length() + 1 ; i++) {
            for (int j = 0 ; j < i ; j++) {
                if (checked[j] && dict.contains(str.substring(j, i))) {
                    checked[i] = true;
                    break;
                }
            }
        }
        return checked[str.length()];
    }

    public static void main(String[] args) {
        System.out.println(wordBreak("leetcode",
                new HashSet<String>(Arrays.asList("leet", "code"))));

        System.out.println(wordBreak("catsandog",
                new HashSet<String>(Arrays.asList("cats", "dog", "sand", "and", "cat"))));

        System.out.println(wordBreakII("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                new HashSet<String>(Arrays.asList("a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"))));
    }
}
