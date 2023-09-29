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

	var a, b int
	var d float64
	fmt.Fscan(in, &a, &b, &d)
	d = d / 180 * math.Pi

	var x, y float64
	x = math.Cos(d)*float64(a) - math.Sin(d)*float64(b)
	y = math.Sin(d)*float64(a) + math.Cos(d)*float64(b)
	fmt.Fprintln(out, x, y)
}

func main() { run(os.Stdin, os.Stdout) }
