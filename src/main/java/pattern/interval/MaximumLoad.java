package pattern.interval;

import com.sun.tools.javac.util.Pair;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class MaximumLoad {


    public static int findMaximumLoad(List<Job> jobs) {
        jobs.sort(Comparator.comparingInt(i -> i.end));

        int maxLoad = 0;
        PriorityQueue<Job> activeJobs = new PriorityQueue<>(Comparator.comparingInt(i -> i.end));
        for (Job job : jobs) {
            while (!activeJobs.isEmpty() && job.start >= activeJobs.peek().end) {
                activeJobs.poll();
            }
            activeJobs.offer(job);

            maxLoad = Math.max(maxLoad, getActiveJobsLoad(activeJobs));
        }
        return maxLoad;
    }

    private static int getActiveJobsLoad(PriorityQueue<Job> activeJobs) {
        return activeJobs.stream().mapToInt(i -> i.load).sum();
    }

    public static void main(String[] args) {
        System.out.println(findMaximumLoad( // 7
                Arrays.asList(
                        new Job(1,4,3),
                        new Job(2,5,4),
                        new Job(7,9,6))
        ));

        System.out.println(findMaximumLoad( // 15
                Arrays.asList(
                        new Job(6,7,10),
                        new Job(2,4,11),
                        new Job(8,12,15))
        ));

        System.out.println(findMaximumLoad( // 8
                Arrays.asList(
                        new Job(1,4,2),
                        new Job(2,4,1),
                        new Job(3,6,5))
        ));
    }
}

class Job {
    int start;
    int end;
    int load;

    public Job(int start, int end, int load) {
        this.start = start;
        this.end = end;
        this.load = load;
    }
}
