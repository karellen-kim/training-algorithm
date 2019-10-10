package leetcode;

/**
 * @author karellen
 */
public class ClimbingStairs {

    public static int countWays(int stairs) {
        return countWaysImpl(stairs, new int[]{1, 2});
    }

    public static int countWaysImpl(int remainStairs, int[] steps) {
        if (remainStairs < 0) {
            return 0;
        } else if (remainStairs == 0) {
            return 1;
        }

        int ways = 0;
        for (int step : steps) {
            ways += countWaysImpl(remainStairs - step, steps);
        }
        return ways;
    }

    public static int countWaysBottomUp(int stairs) {
        int[] dp = new int[stairs + 1];

        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3 ; i <= stairs ; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }
        return dp[stairs];
    }

    public static void main(String[] args) {
        System.out.println(countWays(3));
        System.out.println(countWaysBottomUp(3));
    }
}
