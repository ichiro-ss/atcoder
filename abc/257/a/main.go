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

	var n, x int
	fmt.Fscan(in, &n, &x)
	res := int((x - 1) / n)
	fmt.Fprintln(out, string(65+res))
}

func main() { run(os.Stdin, os.Stdout) }
