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
	a := make([]string, n)
	for i := 0; i < n; i++ {
		var val string
		fmt.Fscan(in, &val)
		a[i] = val
	}
	res := "correct"
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if i == j {
				if a[i][j] != '-' {
					res = "incorrect"
					break
				}
			} else {
				if a[i][j] == 'W' {
					if a[j][i] != 'L' {
						res = "incorrect"
						break
					}
				} else if a[i][j] == 'L' {
					if a[j][i] != 'W' {
						res = "incorrect"
						break
					}
				} else {
					if a[j][i] != 'D' {
						res = "incorrect"
						break
					}
				}
			}
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
