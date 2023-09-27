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

	var n, m, x, t, d int
	fmt.Fscan(in, &n, &m, &x, &t, &d)

	var res int
	res = t
	for i := n; i > m; i-- {
		if !(x < i && i <= n) {
			res -= d
		}
	}
	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
