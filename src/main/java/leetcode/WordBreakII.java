package leetcode;

import java.util.*;
import java.util.stream.Collectors;

/**
 * @author karellen
 */
public class WordBreakII {

    public static List<String> wordBreak(String s, List<String> wordDict) {
        return wordBreakImpl(s, new HashSet<String>(wordDict))
                .stream()
                .map(item -> String.join(" ", item))
                .collect(Collectors.toList());
    }

    private static List<List<String>> wordBreakImpl(String s, Set<String> dict) {
        if (s.isEmpty()) {
            return Arrays.asList(Arrays.asList());
        }

        List<List<String>> result = new ArrayList<>();
        for (String word : dict) {
            if (s.startsWith(word)) {
                List<List<String>> lists = wordBreakImpl(s.substring(word.length()), dict);
                result.addAll(insertWord(word, lists));
            }
        }
        return result;
    }

    private static List<List<String>> insertWord(String word, List<List<String>> list) {
        List<List<String>> result = new ArrayList<>();
        for (List<String> item : list) {
            List<String> newItem = new ArrayList<>();
            newItem.add(word);
            for (String w : item) {
                newItem.add(w);
            }
            result.add(newItem);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(wordBreak("catsanddog",
                Arrays.asList("cat", "cats", "and", "sand", "dog")));

        System.out.println(wordBreak("pineapplepenapple",
                Arrays.asList("apple", "pen", "applepen", "pine", "pineapple")));

        System.out.println(wordBreak("catsandog",
                Arrays.asList("cats", "dog", "sand", "and", "cat")));

        System.out.println(wordBreak("aaaaaaa",
                Arrays.asList("aaaa","aa","a")));

        System.out.println(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                Arrays.asList("a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa")));
    }
}
