package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, k, q int
	fmt.Fscan(in, &n, &k, &q)
	a := make([]int, k)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	l := make([]int, q)
	for i := range l {
		fmt.Fscan(in, &l[i])
	}

	for i := 0; i < q; i++ {
		square := a[l[i]-1]
		if square < n {
			if l[i] == k {
				a[l[i]-1] += 1
			} else if a[l[i]]-square > 1 {
				a[l[i]-1] += 1
			}
		}
	}
	var res string
	for i := 0; i < k; i++ {
		res += (strconv.Itoa(a[i]) + " ")
	}
	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
