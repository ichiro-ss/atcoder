package main

import "fmt"

func main() {
	var x, a, d, n int
	fmt.Scanf("%d %d %d %d", &x, &a, &d, &n)
	res := 0

	if d < 0 {
		a = a + (d * (n - 1))
		d = -d
	}

	l := a + d*(n-1)

	if x <= a {
		res = a - x
	} else if l <= x {
		res = x - l
	} else {
		for i := 0; i < 1000000; i++ {
			if (x+i-a)%d == 0 {
				res = i
				break
			} else if (x-i-a)%d == 0 {
				res = i
				break
			}
		}
	}
	fmt.Println(res)
}
