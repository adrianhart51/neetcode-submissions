func maxAreaOfIsland(grid [][]int) int {
    m := len(grid)
	n := len(grid[0])

	// track visited island
	visited := make(map[[2]int]bool)

	directions := [][2]int{
		{0, 1},
		{0, -1},
		{1, 0},
		{-1, 0},
	}

	// dfs calculate island size
	var dfs func(int, int) int

	dfs = func(row int, col int) int {
		// check if outside boundary or visit not land or already visited return 0 size

		cell := [2]int{row, col}
		if row < 0 || row >= m || col < 0 || col >= n || grid[row][col] != 1 || visited[cell] {
			return 0
		}

		// if visit island size +1
		visited[cell] = true
		result := 1
		// and plus size from dfs visit top, bottom, right, left
		for _, direction := range directions {
			dr := row + direction[0]
			dc := col + direction[1]
			result += dfs(dr, dc)
		}

		return result
	}

	//track max island size
	maxSize := 0

	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
		//	dfs calculate island size
		//	compare with max size
			maxSize = max(maxSize, dfs(r, c))
		}
	}

	return maxSize
}
