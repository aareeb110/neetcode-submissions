/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    minMeetingRooms(intervals) {
        if (intervals.length === 0) return 0;

        const starts = intervals.map(i => i.start).sort((a, b) => a - b);
        const ends = intervals.map(i => i.end).sort((a, b) => a - b);

        let roomsInUse = 0;
        let maxRooms = 0;
        let i = 0;
        let j = 0;

        while (i < starts.length) {
            if (starts[i] < ends[j]) {
                roomsInUse++;
                maxRooms = Math.max(maxRooms, roomsInUse);
                i++;
            } else {
                roomsInUse--;
                j++;
            }
        }
        return maxRooms;
    }
}
