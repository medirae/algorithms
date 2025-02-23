/*
 * @lc app=leetcode id=207 lang=golang
 *
 * [207] Course Schedule
 *
 * https://leetcode.com/problems/course-schedule/description/
 *
 * algorithms
 * Medium (48.28%)
 * Likes:    16826
 * Dislikes: 781
 * Total Accepted:    1.9M
 * Total Submissions: 4M
 * Testcase Example:  '2\n[[1,0]]'
 *
 * There are a total of numCourses courses you have to take, labeled from 0 to
 * numCourses - 1. You are given an array prerequisites where prerequisites[i]
 * = [ai, bi] indicates that you must take course bi first if you want to take
 * course ai.
 *
 *
 * For example, the pair [0, 1], indicates that to take course 0 you have to
 * first take course 1.
 *
 *
 * Return true if you can finish all courses. Otherwise, return false.
 *
 *
 * Example 1:
 *
 *
 * Input: numCourses = 2, prerequisites = [[1,0]]
 * Output: true
 * Explanation: There are a total of 2 courses to take.
 * To take course 1 you should have finished course 0. So it is possible.
 *
 *
 * Example 2:
 *
 *
 * Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
 * Output: false
 * Explanation: There are a total of 2 courses to take.
 * To take course 1 you should have finished course 0, and to take course 0 you
 * should also have finished course 1. So it is impossible.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= numCourses <= 2000
 * 0 <= prerequisites.length <= 5000
 * prerequisites[i].length == 2
 * 0 <= ai, bi < numCourses
 * All the pairs prerequisites[i] are unique.
 *
 *
 */

// @lc code=start
package main

func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make(map[int]map[int]bool)
	indegree := make(map[int]int)
	for course := 0; course < numCourses; course++ {
		graph[course] = make(map[int]bool)
	}
	for _, preq := range prerequisites {
		graph[preq[1]][preq[0]] = true
		indegree[preq[0]]++
		if _, exists := graph[preq[0]][preq[1]]; exists {
			return false
		}
	}

	var indegreeNonzeroCount int
	for course, degree := range indegree {
		if degree > 0 {
			indegreeNonzeroCount++
			continue
		}
		stack := []int{course}
		visited := make(map[int]bool)
		for len(stack) > 0 {
			node := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			visited[node] = true
			for neighbor, _ := range graph[node] {
				if _, exists := visited[node]; exists {
					return false
				}
				stack = append(stack, neighbor)
			}
		}
	}
	return indegreeNonzeroCount != len(graph)
}

// @lc code=end
