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

	var n, m int
	fmt.Fscan(in, &n, &m)

	u := make([]int, m)
	v := make([]int, m)
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &u[i], &v[i])
	}

	adj := make([][]bool, n)
	for i := 0; i < n; i++ {
		adj[i] = make([]bool, n)
	}
	for i := 0; i < m; i++ {
		adj[u[i]-1][v[i]-1] = true
		adj[v[i]-1][u[i]-1] = true
	}

	res := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				if adj[i][j] && adj[j][k] && adj[k][i] {
					res += 1
				}
			}
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
