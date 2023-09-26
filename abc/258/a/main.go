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

	var k int
	fmt.Fscan(in, &k)

	h := 21
	m := 0

	var res string
	if k >= 60 {
		k -= 60
		h++
	}
	m += k

	res = strconv.Itoa(h) + ":"
	if 0 <= m && m < 10 {
		res += ("0" + strconv.Itoa(m))
	} else {
		res += strconv.Itoa(m)
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
