package pattern.interval;

import com.sun.tools.javac.util.Pair;
import utils.ArrayUtils;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class MeetingRooms {

    /**
     * First Solution : Store All Room Schedule
     */
    public static int findMinimumMeetingRoomCount(List<Pair<Integer, Integer>> meetingSchedule) {
        meetingSchedule.sort(Comparator.comparingInt(i -> i.fst));

        List<Pair<Integer, Integer>> roomSchedules = new ArrayList<>();
        roomSchedules.add(meetingSchedule.get(0));
        Pair<Integer, Integer> cur = null;
        for (int i = 1 ; i < meetingSchedule.size() ; i++) {
            cur = meetingSchedule.get(i);

            boolean found = false;
            for (int j = 0 ; j < roomSchedules.size() ; j++) {
                Pair<Integer, Integer> room = roomSchedules.get(j);
                if (!isOverlapped(cur, room)) {
                    roomSchedules.set(j, Pair.of(Math.min(room.fst, cur.fst), Math.max(room.snd, cur.snd)));
                    found = true;
                    break;
                }
            }
            if (!found) {
                roomSchedules.add(cur);
            }
        }
        return roomSchedules.size();
    }

    /**
     * Second Solution : Keep Current Active Meeting Room
     */
    public static int findMinimumMeetingRoomCountII(List<Pair<Integer, Integer>> meetingSchedule) {
        meetingSchedule.sort(Comparator.comparingInt(i -> i.fst));

        int count = 0;
        PriorityQueue<Pair<Integer, Integer>> minHeap = new PriorityQueue<>(Comparator.comparingInt(i -> i.snd));
        for (Pair<Integer, Integer> schedule : meetingSchedule) {
            while (!minHeap.isEmpty() && schedule.fst >= minHeap.peek().snd) {
                minHeap.poll();
            }
            minHeap.offer(schedule);
            count = Math.max(count, minHeap.size());
        }
        return count;
    }

    private static boolean isOverlapped(Pair<Integer, Integer> item1, Pair<Integer, Integer> item2) {
        return (item1.fst > item2.fst && item1.fst < item2.snd)
                || (item2.fst > item1.fst && item2.fst < item1.snd);
    }

    public static void main(String[] args) {
        System.out.println(findMinimumMeetingRoomCount(
                ArrayUtils.convertToPair(new int[][]{{ 6, 7 }, { 2, 4 },  { 8, 12 }}) // 1
        ));
        System.out.pri9ntln(findMinimumMeetingRoomCount(
                ArrayUtils.convertToPair(new int[][]{{ 1, 4 }, { 2, 5 }, { 7, 9 }}) // 2
        ));
        System.out.println(findMinimumMeetingRoomCount(
                ArrayUtils.convertToPair(new int[][]{{ 1, 4 }, { 2, 3 }, { 3, 6 }}) // 2
        ));
        System.out.println(findMinimumMeetingRoomCount(
                ArrayUtils.convertToPair(new int[][]{{ 4, 5 }, { 2, 3 }, { 2, 4 }, { 3, 5 }}) // 2
        ));

        System.out.println(findMinimumMeetingRoomCountII(
                ArrayUtils.convertToPair(new int[][]{{ 6, 7 }, { 2, 4 },  { 8, 12 }}) // 1
        ));
        System.out.println(findMinimumMeetingRoomCountII(
                ArrayUtils.convertToPair(new int[][]{{ 1, 4 }, { 2, 5 }, { 7, 9 }}) // 2
        ));
        System.out.println(findMinimumMeetingRoomCountII(
                ArrayUtils.convertToPair(new int[][]{{ 1, 4 }, { 2, 3 }, { 3, 6 }}) // 2
        ));
        System.out.println(findMinimumMeetingRoomCountII(
                ArrayUtils.convertToPair(new int[][]{{ 4, 5 }, { 2, 3 }, { 2, 4 }, { 3, 5 }}) // 2
        ));
    }
}
