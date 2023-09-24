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

	var h, w [3]int
	for i := range h {
		fmt.Fscan(in, &h[i])
	}
	for i := range w {
		fmt.Fscan(in, &w[i])
	}

	res := 0
	for a := 1; a < 29; a++ {
		for b := 1; b < 29; b++ {
			for d := 1; d < 29; d++ {
				for e := 1; e < 29; e++ {
					c := h[0] - a - b
					f := h[1] - e - d
					g := w[0] - a - d
					i := w[1] - b - e
					j := w[2] - c - f
					if c > 0 && f > 0 && g > 0 && i > 0 && j > 0 && g+i+j == h[2] {
						res++
					}
				}
			}
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
