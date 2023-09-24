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
	for i := range a {
		fmt.Fscan(in, &a[i])
	}

	res := 0
	var squares [4]bool
	for i := 0; i < n; i++ {
		squares[0] = true
		for j := 3; j > -1; j-- {
			if squares[j] {
				squares[j] = false
				if j+a[i] > 3 {
					res++
				} else {
					squares[j+a[i]] = true
				}
			}
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
