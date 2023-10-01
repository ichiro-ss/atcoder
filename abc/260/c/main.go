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

	var n, x, y int
	fmt.Fscan(in, &n, &x, &y)

	r := make([]int, 12)
	b := make([]int, 12)
	r[0] = 0
	b[0] = 1
	for i := 1; i < n; i++ {
		b[i] = r[i-1] + y*b[i-1]
		r[i] = r[i-1] + x*b[i]
	}

	fmt.Fprintln(out, r[n-1])
}

func main() { run(os.Stdin, os.Stdout) }
