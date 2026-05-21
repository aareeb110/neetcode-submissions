class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        const maxPQ = new MaxPriorityQueue();
        for (const stone of stones) {
            maxPQ.enqueue(stone);
        }

        while (maxPQ.size() > 1) {
            const stoneX = maxPQ.dequeue();
            const stoneY = maxPQ.dequeue();

            if (stoneX !== stoneY) {
                const newStone = Math.abs(stoneX - stoneY);
                maxPQ.enqueue(newStone);
            }
        }

        return maxPQ.size() === 1 ? maxPQ.dequeue() : 0;
    }
}
