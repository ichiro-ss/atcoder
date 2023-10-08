package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, m, t int
	fmt.Fscan(in, &n, &m, &t)
	var x, y int
	a := make([]int, n-1)
	bonus := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		fmt.Fscan(in, &a[i])
	}
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &x, &y)
		bonus[x-1] = y
	}

	res := "Yes"
	for i := 0; i < n-1; i++ {
		t -= a[i]
		t += bonus[i]
		if t < 0 {
			res = "No"
			break
		}
		fmt.Fprintln(out, t)
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
