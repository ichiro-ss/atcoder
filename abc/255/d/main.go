package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, q int
	fmt.Fscan(in, &n, &q)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	sort.Ints(a)

	asum := make([]int64, len(a))
	asum[0] = int64(a[0])
	for i := 1; i < n; i++ {
		asum[i] = asum[i-1] + int64(a[i])
	}

	var k int
	var res int64
	var x int
	for i := 0; i < q; i++ {
		fmt.Fscan(in, &x)
		k = sort.SearchInts(a, x)
		if k >= len(asum) {
			res = int64(k*x) - asum[k-1]
		} else if k == 0 {
			res = asum[len(asum)-1] - int64(len(asum)*x)
		} else {
			res = int64(k*x) - asum[k-1] + asum[len(asum)-1] - asum[k-1] - int64((len(asum)-k)*x)
			// fmt.Println("k:", k, "--", k*x[i], "-", asum[k], "+", asum[len(asum)-1], "-", asum[k-1], "-", k*x[i])
		}
		fmt.Fprintln(out, res)
	}
}

func main() { run(os.Stdin, os.Stdout) }
