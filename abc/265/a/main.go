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

	var x, y, n int
	fmt.Fscan(in, &x, &y, &n)

	var res int
	if x*3 > y {
		res += (n / 3) * y
		n -= (n / 3) * 3
	}

	res += n * x

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
