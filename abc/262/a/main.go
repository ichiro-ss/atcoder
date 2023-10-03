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

	var y int
	fmt.Fscan(in, &y)
	mod := y % 4

	res := y
	if mod == 0 {
		res += 2
	} else if mod == 1 {
		res += 1
	} else if mod == 3 {
		res += 3
	}
	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
