func subsets(nums []int) [][]int {
	result := [][]int{}
	path := []int{}

	var dfs func(int)

	dfs = func(i int) {
		//	check if i already reach end of nums, if yes add path to result
		//	means already consider take or skip num until end of nums
		if i == len(nums) {
			temp := make([]int, len(path))
			copy(temp, path)
			result = append(result, temp)
			return
		}

		//	add nums[i] to path
		//	dfs next index with nums[i]
		path = append(path, nums[i])
		dfs(i + 1)

		//	backtrack remove nums[i] from path
		//	dfs next index without nums[i]
		path = path[:len(path)-1]
		dfs(i + 1)
	}

	dfs(0)

	return result
}
