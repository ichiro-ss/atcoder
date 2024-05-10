package main

import (
	"fmt"
	"io"
	"math"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

// 貪欲：連結成分の小さい順に結合していく
func gComponentNum(numCity, numSp int, linkWith [][]int) []int {
	uf := newUnionFind(numCity)

	// 連結成分をk-l回結合
	for i := 0; i < numCity-numSp; i++ {
		minSize := 1000000
		mergeJ, mergeLink := -1, -1
		for j := 0; j < numCity; j++ {
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
	cnt := 0
	for i := 0; i < numCity; i++ {
		root := uf.find(i)
		if _, ok := city20[root]; !ok {
			city20[root] = cnt
			cnt++
		}
	}
	res := make([]int, numCity)
	for i := 0; i < numCity; i++ {
		root := uf.find(i)
		res[i] = city20[root]
	}
	return res
}

// 連結成分をまとめる
func connectComponent(numSquare, numCity int, city [][]int) *[][]int {
	dir := [4][2]int{{0, 1}, {1, 0}}
	linkWith := make([][]int, numCity)
	isLinked := make([][]bool, numCity)
	for i := 0; i < numCity; i++ {
		isLinked[i] = make([]bool, numCity)
	}
	for i := 0; i < numSquare; i++ {
		for j := 0; j < numSquare; j++ {
			if city[i][j] < 0 {
				continue
			}
			for _, d := range dir {
				x, y := i+d[0], j+d[1]
				if x >= 0 && x < numSquare && y >= 0 && y < numSquare {
					if city[i][j] == city[x][y] || city[x][y] < 0 {
						continue
					}
					if !isLinked[city[i][j]][city[x][y]] {
						linkWith[city[i][j]] = append(linkWith[city[i][j]], city[x][y])
						linkWith[city[x][y]] = append(linkWith[city[x][y]], city[i][j])
						isLinked[city[i][j]][city[x][y]] = true
						isLinked[city[x][y]][city[i][j]] = true
					}
				}
			}
		}
	}
	return &linkWith
}

func dfs(c int, res []int, visited *[]bool, linkWith [][]int) {
	(*visited)[c] = true
	for _, linkCity := range linkWith[c] {
		if res[linkCity] == res[c] && !(*visited)[linkCity] {
			dfs(linkCity, res, visited, linkWith)
		}
	}
}

func getScore(numCity, numSp int, res []int, numPpl, numEmp []int, linkWith [][]int) (int, int, int, int, float64) {
	visited := make([]bool, numCity)
	for i := 0; i < numSp; i++ {
		c := -1
		for j := 0; j < numCity; j++ {
			if res[j] == i {
				c = j
			}
		}
		if c == -1 {
			// fmt.Println("sp not exist")
			return -1, -1, -1, -1, 0
		}
		dfs(c, res, &visited, linkWith)
	}
	for i := 0; i < numCity; i++ {
		if !visited[i] {
			// fmt.Println("not connected")
			return -1, -1, -1, -1, 0
		}
	}

	p, q := make([]int, numSp), make([]int, numSp)
	for i := 0; i < numCity; i++ {
		p[res[i]] += numPpl[i]
		q[res[i]] += numEmp[i]
	}

	pMinIdx, pMin := arrayMin(p)
	pMaxIdx, pMax := arrayMax(p)
	qMinIdx, qMin := arrayMin(q)
	qMaxIdx, qMax := arrayMax(q)

	return pMinIdx, pMaxIdx, qMinIdx, qMaxIdx, math.Min(float64(pMin)/float64(pMax), float64(qMin)/float64(qMax))
}

func main() {
	TIMELIMIT := 0.95
	st := time.Now()
	// n, k, l, a, b, c := input(getStdin())
	numSquare, numCity, numSp, numPpl, numEmp, city := input(getStdin())

	linkWith := *connectComponent(numSquare, numCity, city)

	res := gComponentNum(numCity, numSp, linkWith)
	bestRes := make([]int, numCity)
	copy(bestRes, res)

	_, _, _, _, curScore := getScore(numCity, numSp, res, numPpl, numEmp, linkWith)
	for time.Since(st).Seconds() < TIMELIMIT {
		for {
			// fmt.Println("kick:", curScore)
			randCity := rand.Intn(numCity)
			l := linkWith[randCity][rand.Intn(len(linkWith[randCity]))]
			resRandCity := res[randCity]
			resL := res[l]
			res[randCity], res[l] = resL, resRandCity
			_, _, _, _, nowScore := getScore(numCity, numSp, res, numPpl, numEmp, linkWith)
			if res[randCity] != res[l] && nowScore > 0 {
				_, _, _, _, curScore = getScore(numCity, numSp, res, numPpl, numEmp, linkWith)
				break
			} else {
				res[randCity], res[l] = resRandCity, resL
			}
			if time.Since(st).Seconds() > TIMELIMIT {
				break
			}
		}
		for {
			isResChanged := false
			randCities := make([]int, numCity)
			for i := 0; i < numCity; i++ {
				randCities[i] = i
			}
			rand.Shuffle(numCity, func(i, j int) {
				randCities[i], randCities[j] = randCities[j], randCities[i]
			})
			for c1 := range randCities {
				for linkCity := range linkWith[c1] {
					if res[c1] == res[linkCity] {
						continue
					}
					oldSp := res[c1]
					res[c1] = res[linkCity]
					_, _, _, _, newScore := getScore(numCity, numSp, res, numPpl, numEmp, linkWith)
					// if newScore > 0.3 {
					// 	fmt.Println("shift", c1, ":", oldSp, "->", res[c1])
					// }
					if newScore > curScore {
						// fmt.Println("ls:", curScore)
						curScore = newScore
						isResChanged = true
					} else {
						res[c1] = oldSp
					}

					if time.Since(st).Seconds() > TIMELIMIT {
						break
					}
				}
			}
			if !isResChanged {
				break
			}
		}
		if _, _, _, _, score := getScore(numCity, numSp, bestRes, numPpl, numEmp, linkWith); curScore > score {
			copy(bestRes, res)
		}
	}
	output(numCity, numSp, bestRes)
}

// check if ans is valid
func isValid(numCity, numSp int, ans []int) bool {
	res := true
	if len(ans) != numCity {
		fmt.Println("len(ans) != K(400)")
		res = false
	}
	for _, a := range ans {
		if a < 0 || a > numSp-1 {
			fmt.Println("a < 1 || a > L(20)")
			res = false
		}
	}
	isExist := make([]bool, numSp)
	for _, a := range ans {
		isExist[a] = true
	}
	for i := 0; i < numSp; i++ {
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
	numSquare, _ := strconv.Atoi(line0[0])
	numCity, _ := strconv.Atoi(line0[1])
	numSp, _ := strconv.Atoi(line0[2])

	numPpl := make([]int, numCity)
	numEmp := make([]int, numCity)
	for i, line := range lines[1 : numCity+1] {
		ab := strings.Split(line, " ")
		numPpl[i], _ = strconv.Atoi(ab[0])
		numEmp[i], _ = strconv.Atoi(ab[1])
	}

	city := make([][]int, numSquare)
	for i, line := range lines[numCity+1:] {
		city[i] = make([]int, numSquare)
		for j, s := range strings.Split(line, " ") {
			city[i][j], _ = strconv.Atoi(s)
			city[i][j]--
		}
	}

	return numSquare, numCity, numSp, numPpl, numEmp, city
}

func output(numCity, numSp int, res []int) {
	if isValid(numCity, numSp, res) {
		for _, r := range res {
			fmt.Println(r + 1)
		}
	}
}

func arrayMin(a []int) (int, int) {
	min := a[0]
	idx := 0
	for i, v := range a {
		if v < min {
			min = v
			idx = i
		}
	}
	return idx, min
}
func arrayMax(a []int) (int, int) {
	max := a[0]
	idx := 0
	for i, v := range a {
		if v > max {
			max = v
			idx = i
		}
	}
	return idx, max
}
