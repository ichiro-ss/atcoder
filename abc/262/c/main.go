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
	a := make([]int, n)
	same := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i])
		a[i]--
		if a[i] == i {
			same++
		}
	}

	res := same * (same - 1) / 2
	for i := 0; i < n; i++ {
		if a[i] > i && a[a[i]] == i {
			res++
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
