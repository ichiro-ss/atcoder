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

	var a, b, c, d, e int
	fmt.Fscan(in, &a, &b, &c, &d, &e)

	res := "Yes"
	count := make([]int, 13)
	count[a-1]++
	count[b-1]++
	count[c-1]++
	count[d-1]++
	count[e-1]++

	for i := 0; i < len(count); i++ {
		if count[i] != 2 && count[i] != 3 && count[i] != 0 {
			res = "No"
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
