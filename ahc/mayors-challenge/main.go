package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// 貪欲：連結成分の小さい順に結合していく
func gComponentNum(n, k, l int, c [][]int) []int {
	uf := newUnionFind(k)
	linkWith := *connectComponent(n, k, c)

	// 連結成分をk-l回結合
	for i := 0; i < k-l; i++ {
		minSize := 1000000
		mergeJ, mergeLink := -1, -1
		for j := 0; j < k; j++ {
			for _, link := range linkWith[j] {
				if !uf.isSame(j, link) {
					sizeJ, sizeLink := uf.size(j), uf.size(link)
					if sizeJ+sizeLink < minSize {
						minSize = sizeJ + sizeLink
						mergeJ, mergeLink = j, link
					}
				}
			}
		}
		// fmt.Println("merge", mergeJ, mergeLink)
		uf.union(mergeJ, mergeLink)
	}

	// root : idx
	city20 := make(map[int]int)
	cnt := 1
	for i := 0; i < k; i++ {
		root := uf.find(i)
		if _, ok := city20[root]; !ok {
			city20[root] = cnt
			cnt++
		}
	}
	res := make([]int, k)
	for i := 0; i < k; i++ {
		root := uf.find(i)
		res[i] = city20[root]
	}
	return res
}

// 連結成分をまとめる
func connectComponent(n, k int, c [][]int) *[][]int {
	dir := [4][2]int{{0, 1}, {1, 0}}
	linkWith := make([][]int, k)
	isLinked := make([][]bool, k)
	for i := 0; i < k; i++ {
		isLinked[i] = make([]bool, k)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if c[i][j] < 0 {
				continue
			}
			for _, d := range dir {
				x, y := i+d[0], j+d[1]
				if x >= 0 && x < n && y >= 0 && y < n {
					if c[i][j] == c[x][y] || c[x][y] < 0 {
						continue
					}
					if !isLinked[c[i][j]][c[x][y]] {
						linkWith[c[i][j]] = append(linkWith[c[i][j]], c[x][y])
						linkWith[c[x][y]] = append(linkWith[c[x][y]], c[i][j])
						isLinked[c[i][j]][c[x][y]] = true
						isLinked[c[x][y]][c[i][j]] = true
					}
				}
			}
		}
	}
	return &linkWith
}

func main() {
	// n, k, l, a, b, c := input(getStdin())
	n, k, l, _, _, c := input(getStdin())

	ans := gComponentNum(n, k, l, c)

	output(k, l, ans)
}

// check if ans is valid
func isValid(k, l int, ans []int) bool {
	res := true
	if len(ans) != k {
		fmt.Println("len(ans) != K(400)")
		res = false
	}
	for _, a := range ans {
		if a < 1 || a > l {
			fmt.Println("a < 1 || a > L(20)")
			res = false
		}
	}
	isExist := make([]bool, l)
	for _, a := range ans {
		isExist[a-1] = true
	}
	for i := 0; i < l; i++ {
		if !isExist[i] {
			fmt.Println(i+1, "city is not used")
			res = false
		}
	}
	return res
}

type UnionFind struct {
	n    int
	root []int
}

func newUnionFind(n int) UnionFind {
	root := make([]int, n)
	for i := 0; i < n; i++ {
		root[i] = -1
	}
	uf := UnionFind{n: n, root: root}
	return uf
}
func (u *UnionFind) find(x int) int {
	if u.root[x] < 0 {
		return x
	}
	u.root[x] = u.find(u.root[x])
	return u.root[x]
}
func (u *UnionFind) union(x, y int) {
	x = u.find(x)
	y = u.find(y)
	if x == y {
		return
	}
	if -u.root[x] < -u.root[y] {
		x, y = y, x
	} // xの方がサイズ大きいように
	u.root[x] += u.root[y]
	u.root[y] = x
}
func (u *UnionFind) isSame(x, y int) bool {
	return u.find(x) == u.find(y)
}
func (u *UnionFind) size(x int) int {
	return -u.root[u.find(x)]
}

func getStdin() []string {
	stdin, _ := io.ReadAll(os.Stdin)
	return strings.Split(strings.TrimRight(string(stdin), "\n"), "\n")
}

func input(lines []string) (int, int, int, []int, []int, [][]int) {
	line0 := strings.Split(lines[0], " ")
	n, _ := strconv.Atoi(line0[0])
	k, _ := strconv.Atoi(line0[1])
	l, _ := strconv.Atoi(line0[2])

	a := make([]int, k)
	b := make([]int, k)
	for i, line := range lines[1 : k+1] {
		ab := strings.Split(line, " ")
		a[i], _ = strconv.Atoi(ab[0])
		b[i], _ = strconv.Atoi(ab[1])
	}

	c := make([][]int, n)
	for i, line := range lines[k+1:] {
		c[i] = make([]int, n)
		for j, s := range strings.Split(line, " ") {
			c[i][j], _ = strconv.Atoi(s)
			c[i][j]--
		}
	}

	return n, k, l, a, b, c
}

func output(k, l int, ans []int) {
	if isValid(k, l, ans) {
		for _, a := range ans {
			fmt.Println(a)
		}
	}
}
