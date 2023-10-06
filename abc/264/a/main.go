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

	var l, r int
	fmt.Fscan(in, &l, &r)

	atcoder := "atcoder"

	fmt.Fprintln(out, atcoder[l-1:r])
}

func main() { run(os.Stdin, os.Stdout) }
