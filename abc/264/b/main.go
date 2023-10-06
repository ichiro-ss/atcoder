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

	var r, c int
	fmt.Fscan(in, &r, &c)

	res := "black"
	dist := math.Max(math.Abs(float64(8-r)), math.Abs(float64(8-c)))

	if int(dist)%2 == 0 {
		res = "white"
	}
	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
