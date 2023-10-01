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

	var n, x, y, z int
	fmt.Fscan(in, &n, &x, &y, &z)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	b := make([]int, n)
	for i := range b {
		fmt.Fscan(in, &b[i])
	}

	is_passed := make([]bool, n)
	res_x := make([][]int, n)
	for i := 0; i < n; i++ {
		res_x[i] = []int{i, a[i], b[i]}
	}
	sort.SliceStable(res_x, func(i, j int) bool { return res_x[i][1] > res_x[j][1] })
	res_y := res_x[x:]
	sort.Slice(res_y, func(i, j int) bool { return res_y[i][0] < res_y[j][0] })
	sort.SliceStable(res_y, func(i, j int) bool { return res_y[i][2] > res_y[j][2] })
	res_z := res_y[y:]
	sort.Slice(res_z, func(i, j int) bool { return res_z[i][0] < res_z[j][0] })
	sort.SliceStable(res_z, func(i, j int) bool { return res_z[i][1]+res_z[i][2] > res_z[j][1]+res_z[j][2] })
	// fmt.Fprintln(out, res_x)
	// fmt.Fprintln(out, res_y)
	// fmt.Fprintln(out, res_z)

	for i := 0; i < x; i++ {
		is_passed[res_x[i][0]] = true
	}
	for i := 0; i < y; i++ {
		is_passed[res_y[i][0]] = true
	}
	for i := 0; i < z; i++ {
		is_passed[res_z[i][0]] = true
	}

	for i := 0; i < n; i++ {
		if is_passed[i] {
			fmt.Fprintln(out, i+1)
		}
	}
}

func main() { run(os.Stdin, os.Stdout) }
