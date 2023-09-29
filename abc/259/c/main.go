package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

type rle struct {
	alphabet byte
	length   int
}

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var s, t string
	fmt.Fscan(in, &s)
	fmt.Fscan(in, &t)

	res := "Yes"
	s_slice := []rle{{s[0], 1}}
	t_slice := []rle{{t[0], 1}}
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			s_slice[len(s_slice)-1].length++
		} else {
			s_slice = append(s_slice, rle{alphabet: s[i], length: 1})
		}
	}
	for i := 1; i < len(t); i++ {
		if t[i] == t[i-1] {
			t_slice[len(t_slice)-1].length++
		} else {
			t_slice = append(t_slice, rle{alphabet: t[i], length: 1})
		}
	}

	if len(s_slice) != len(t_slice) {
		res = "No"
	} else {
		for i := 0; i < len(s_slice); i++ {
			if s_slice[i].alphabet != t_slice[i].alphabet {
				res = "No"
			}
			if !(s_slice[i].length == t_slice[i].length || s_slice[i].length < t_slice[i].length && s_slice[i].length >= 2) {
				res = "No"
			}
		}
	}

	fmt.Fprintln(out, res)
}

func main() { run(os.Stdin, os.Stdout) }
