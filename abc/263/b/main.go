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

	var n int
	fmt.Fscan(in, &n)
	p := make([]int, n)
	for i := 1; i < n; i++ {
		fmt.Fscan(in, &p[i])
	}

	res := 0
	now := n
	for now != 0 {
		res++
		now = p[now-1]
	}
	fmt.Fprintln(out, res-1)
}

func main() { run(os.Stdin, os.Stdout) }
