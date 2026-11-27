func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	// use dijkstra to get cheapest price but need to check k limit

	// convert flights to graph adjacency list
	graph := make(map[int][][2]int)
	for _, f := range flights {
		graph[f[0]] = append(graph[f[0]], [2]int{f[1], f[2]})
	}

	// create priority queue cheaper cost
	// start with source with 0 cost and stop
	pq := &FlightHeap{
		{
			Cost:        0,
			Destination: src,
			Stops:       0,
		},
	}

	heap.Init(pq)

	best := make(map[[2]int]int)

	for pq.Len() > 0 {
		curr := heap.Pop(pq).(Flight)

		// if reach destination store cheaper price
		if curr.Destination == dst {
			return curr.Cost
		}

		// if stop count > k stop explore try other path
		if curr.Stops > k {
			continue
		}

		key := [2]int{curr.Destination, curr.Stops}
		if v, ok := best[key]; ok && v <= curr.Cost {
			continue
		}
		best[key] = curr.Cost

		// visit next cheapest destination
		for _, next := range graph[curr.Destination] {
			newCost := curr.Cost + next[1]
			heap.Push(pq, Flight{
				Cost:        newCost,
				Destination: next[0],
				Stops:       curr.Stops + 1,
			})
		}
	}

	return -1
}

type Flight struct {
	Cost        int
	Destination int
	Stops       int
}

type FlightHeap []Flight

func (f FlightHeap) Len() int {
	return len(f)
}

func (f FlightHeap) Less(i, j int) bool {
	return f[i].Cost < f[j].Cost
}

func (f FlightHeap) Swap(i, j int) {
	f[i], f[j] = f[j], f[i]
}

func (f *FlightHeap) Push(x any) {
	*f = append(*f, x.(Flight))
}

func (f *FlightHeap) Pop() any {
	old := *f
	n := len(old)
	x := old[n-1]
	*f = old[:n-1]

	return x
}