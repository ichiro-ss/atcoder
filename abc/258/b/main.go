package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		var row string
		fmt.Fscan(in, &row)
		row_strs := strings.Split(row, "")
		row_ints := make([]int, n)
		for j := 0; j < n; j++ {
			row_ints[j], _ = strconv.Atoi(row_strs[j])
		}
		a[i] = row_ints
	}

	dists := [8][2]int{{0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}}
	var res int
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < 8; k++ {
				now := 0
				x := i
				y := j
				for l := 0; l < n; l++ {
					now *= 10
					now += a[x][y]
					x = (x + dists[k][0] + n) % n
					y = (y + dists[k][1] + n) % n
				}
				if res < now {
					res = now
				}
			}
		}
	}
	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
