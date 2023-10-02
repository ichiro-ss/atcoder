package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var l1, r1, l2, r2 float64
	fmt.Fscan(in, &l1, &r1, &l2, &r2)

	res := math.Max(0, math.Min(r1, r2)-math.Max(l1, l2))

	fmt.Fprintln(out, int(res))
}

func main() { run(os.Stdin, os.Stdout) }
