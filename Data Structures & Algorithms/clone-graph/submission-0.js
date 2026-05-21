/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        if (!node) {
            return null;
        }

        const map = new Map();

        const dfs = (node) => {
            if (map.has(node)) {
                return map.get(node);
            }

            const cloneNode = new Node(node.val);
            map.set(node, cloneNode);

            for (const neighbor of node.neighbors) {
                cloneNode.neighbors.push(dfs(neighbor));
            }

            return cloneNode;
        };

        return dfs(node);
    }
}
