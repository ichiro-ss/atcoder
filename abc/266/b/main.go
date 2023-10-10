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

	x := 0
	for x < 998244354 {
		if (n-x)%998244353 == 0 {
			break
		}
		x++
	}

	fmt.Fprintln(out, x)
}

func main() { run(os.Stdin, os.Stdout) }
