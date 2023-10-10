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

	var s string
	fmt.Fscan(in, &s)
	n := len(s)
	m := n / 2

	fmt.Fprintln(out, string(s[m]))
}

func main() { run(os.Stdin, os.Stdout) }
