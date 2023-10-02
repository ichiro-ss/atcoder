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

	var n int
	fmt.Fscan(in, &n)
	s := make([]string, n)
	for i := 0; i < n; i++ {
		var val string
		fmt.Fscan(in, &val)
		s[i] = val
	}

	smap := map[string]int{}
	for i := 0; i < n; i++ {
		if smap[s[i]] == 0 {
			fmt.Fprintln(out, s[i])
		} else {
			fmt.Fprintln(out, s[i]+"("+strconv.Itoa(smap[s[i]])+")")
		}
		smap[s[i]]++
	}
}

func main() { run(os.Stdin, os.Stdout) }
