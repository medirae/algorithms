/*
 * @lc app=leetcode id=399 lang=golang
 *
 * [399] Evaluate Division
 *
 * https://leetcode.com/problems/evaluate-division/description/
 *
 * algorithms
 * Medium (62.64%)
 * Likes:    9619
 * Dislikes: 1005
 * Total Accepted:    563.1K
 * Total Submissions: 898K
 * Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
 *
 * You are given an array of variable pairs equations and an array of real
 * numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
 * equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
 * single variable.
 *
 * You are also given some queries, where queries[j] = [Cj, Dj] represents the
 * j^th query where you must find the answer for Cj / Dj = ?.
 *
 * Return the answers to all queries. If a single answer cannot be determined,
 * return -1.0.
 *
 * Note: The input is always valid. You may assume that evaluating the queries
 * will not result in division by zero and that there is no contradiction.
 *
 * Note: The variables that do not occur in the list of equations are
 * undefined, so the answer cannot be determined for them.
 *
 *
 * Example 1:
 *
 *
 * Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
 * [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
 * Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
 * Explanation:
 * Given: a / b = 2.0, b / c = 3.0
 * queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
 * return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
 * note: x is undefined => -1.0
 *
 * Example 2:
 *
 *
 * Input: equations = [["a","b"],["b","c"],["bc","cd"]], values =
 * [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
 * Output: [3.75000,0.40000,5.00000,0.20000]
 *
 *
 * Example 3:
 *
 *
 * Input: equations = [["a","b"]], values = [0.5], queries =
 * [["a","b"],["b","a"],["a","c"],["x","y"]]
 * Output: [0.50000,2.00000,-1.00000,-1.00000]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= equations.length <= 20
 * equations[i].length == 2
 * 1 <= Ai.length, Bi.length <= 5
 * values.length == equations.length
 * 0.0 < values[i] <= 20.0
 * 1 <= queries.length <= 20
 * queries[i].length == 2
 * 1 <= Cj.length, Dj.length <= 5
 * Ai, Bi, Cj, Dj consist of lower case English letters and digits.
 *
 *
*/

// @lc code=start
package main

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	graph := make(map[string]map[string]float64)
	initMap := func(arg string) {
		if _, exists := graph[arg]; !exists {
			graph[arg] = make(map[string]float64)
		}
	}
	for ndx, equation := range equations {
		arg1, arg2 := equation[0], equation[1]
		initMap(arg1)
		initMap(arg2)

		graph[arg1][arg2] = values[ndx]
		if values[ndx] != 0.0 {
			graph[arg2][arg1] = 1 / values[ndx]
		}
	}
	ret := make([]float64, len(queries))
	for ndx, query := range queries {
		arg1, arg2 := query[0], query[1]
		_, arg1Exists := graph[arg1]
		_, arg2Exists := graph[arg2]
		if !arg1Exists || !arg2Exists {
			ret[ndx] = -1.0
			continue
		}

		stackKeys := []string{arg1}
		stackResults := []float64{1.0}
		visited := make(map[string]bool)
		var found bool = false

		for len(stackKeys) > 0 {
			nodeKey := stackKeys[len(stackKeys)-1]
			stackKeys = stackKeys[:len(stackKeys)-1]
			nodeResult := stackResults[len(stackResults)-1]
			stackResults = stackResults[:len(stackResults)-1]

			visited[nodeKey] = true
			if nodeKey == arg2 {
				found = true
				ret[ndx] = nodeResult
				break
			}
			for neighbor, neighborValue := range graph[nodeKey] {
				if _, exists := visited[neighbor]; !exists {
					stackKeys = append(stackKeys, neighbor)
					stackResults = append(stackResults, neighborValue*nodeResult)
				}
			}
		}
		if !found {
			ret[ndx] = -1.0
		}
	}

	return ret
}

// @lc code=end
