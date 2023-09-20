package main

import "fmt"

func main() {
	var r, c int
	var a [2][2]int

	fmt.Scanf("%d %d", &r, &c)
	for i := 0; i < 2; i++ {
		fmt.Scan(&a[i][0], &a[i][1])
	}

	fmt.Printf("%d", a[r-1][c-1])
}
