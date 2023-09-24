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

	var n float64
	fmt.Fscan(in, &n)

	var res float64

	res = math.Pow(2, n)
	fmt.Fprintln(out, int(res))
}

func main() { run(os.Stdin, os.Stdout) }
