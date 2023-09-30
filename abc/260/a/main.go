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

	s_map := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		s_map[s[i]]++
	}
	for i := byte('a'); i <= 'z'; i++ {
		if s_map[i] == 1 {
			fmt.Fprintln(out, string(i))
			return
		}
	}

	fmt.Fprintln(out, -1)
}

func main() { run(os.Stdin, os.Stdout) }
