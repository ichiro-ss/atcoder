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

	var n int
	fmt.Fscan(in, &n)
	var imos [2*100000 + 1]int
	for i := 0; i < n; i++ {
		var l, r int
		fmt.Fscan(in, &l, &r)
		imos[l]++
		imos[r]--
	}

	for i := 1; i < len(imos); i++ {
		imos[i] += imos[i-1]
	}
	is_contained := false
	for i := 0; i < len(imos); i++ {
		if !is_contained {
			if imos[i] > 0 {
				fmt.Printf("%d ", i)
				is_contained = true
				continue
			}
		} else {
			if imos[i] <= 0 {
				fmt.Println(i)
				is_contained = false
			}
		}
	}
}

func main() { run(os.Stdin, os.Stdout) }
