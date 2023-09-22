package main

import (
	"fmt"
	"math"
)

func main() {
	var n, k int
	fmt.Scanf("%d %d", &n, &k)
	var a []int
	var have_light [100000]bool

	for i := 0; i < k; i++ {
		var x int
		fmt.Scanf("%d", &x)
		a = append(a, x-1)
		have_light[x-1] = true
	}
	var x, y []int
	for i := 0; i < n; i++ {
		var b, c int
		fmt.Scanf("%d %d", &b, &c)
		x = append(x, b)
		y = append(y, c)
	}

	max := 0.0
	var dist float64
	for i := 0; i < n; i++ {
		min := math.Pow10(12)
		for j := 0; j < k; j++ {
			dist = math.Pow(float64(x[a[j]]-x[i]), 2.0) + math.Pow(float64(y[a[j]]-y[i]), 2.0)
			min = math.Min(min, dist)
		}
		max = math.Max(max, min)
	}
	fmt.Println(math.Sqrt(max))
}
