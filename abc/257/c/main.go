package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	var s string
	fmt.Fscan(in, &n)
	fmt.Fscan(in, &s)
	w := make([]int, n)
	for i := range w {
		fmt.Fscan(in, &w[i])
	}
	person := make([]struct {
		weight int
		adult  bool
	}, n, n)

	max := 0
	for i := 0; i < n; i++ {
		person[i] = struct {
			weight int
			adult  bool
		}{
			w[i], s[i] == byte('1'),
		}
		if s[i] == byte('1') {
			max++
		}
	}
	sort.Slice(person, func(i, j int) bool { return person[i].weight < person[j].weight })
	tmp := max
	for i, v := range person {
		if v.adult {
			tmp--
		} else {
			tmp++
		}
		if i < n-1 {
			if person[i].weight != person[i+1].weight && max < tmp {
				max = tmp
			}
		} else {
			if max < tmp {
				max = tmp
			}
		}
	}
	fmt.Fprintln(out, max)
}

func main() { run(os.Stdin, os.Stdout) }
