package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	n, a := input(getStdin())
	res := ""
	for i := 0; i < n; i++ {
		if i == n-1 {
			if a[0][i] < 5 {
				res += "PRRRRQLLLLD"
			} else if a[0][i] < 10 {
				res += "PRRRRDQLLLL"
			} else if a[0][i] < 15 {
				res += "PRRRRDDQULLLL"
			} else if a[0][i] < 20 {
				res += "PRRRRDDDQUULLLL"
			} else {
				res += "PRRRRDDDDQUUULLLL"
			}
		} else {
			if a[0][i] < 5 {
				res += "PRRRRQLLLL"
			} else if a[0][i] < 10 {
				res += "PRRRRDQULLLL"
			} else if a[0][i] < 15 {
				res += "PRRRRDDQUULLLL"
			} else if a[0][i] < 20 {
				res += "PRRRRDDDQUUULLLL"
			} else {
				res += "PRRRRDDDDQUUUULLLL"
			}
		}
	}
	for i := 0; i < n; i++ {
		if i == n-1 {
			if a[1][i] < 5 {
				res += "PRRRRUQLLLLDD"
			} else if a[1][i] < 10 {
				res += "PRRRRQLLLLD"
			} else if a[1][i] < 15 {
				res += "PRRRRDQLLLL"
			} else if a[1][i] < 20 {
				res += "PRRRRDDQULLLL"
			} else {
				res += "PRRRRDDDQUULLLL"
			}
		} else {
			if a[1][i] < 5 {
				res += "PRRRRUQLLLLD"
			} else if a[1][i] < 10 {
				res += "PRRRRQLLLL"
			} else if a[1][i] < 15 {
				res += "PRRRRDQULLLL"
			} else if a[1][i] < 20 {
				res += "PRRRRDDQUULLLL"
			} else {
				res += "PRRRRDDDQUUULLLL"
			}
		}
	}
	for i := 0; i < n; i++ {
		if i == n-1 {
			if a[2][i] < 5 {
				res += "PRRRRUUQLLLLDDD"
			} else if a[2][i] < 10 {
				res += "PRRRRUQLLLLDD"
			} else if a[2][i] < 15 {
				res += "PRRRRQLLLLD"
			} else if a[2][i] < 20 {
				res += "PRRRRDQLLLL"
			} else {
				res += "PRRRRDDQULLLL"
			}
		} else {
			if a[2][i] < 5 {
				res += "PRRRRUUQLLLLDD"
			} else if a[2][i] < 10 {
				res += "PRRRRUQLLLLD"
			} else if a[2][i] < 15 {
				res += "PRRRRQLLLL"
			} else if a[2][i] < 20 {
				res += "PRRRRDQULLLL"
			} else {
				res += "PRRRRDDQUULLLL"
			}
		}
	}
	for i := 0; i < n; i++ {
		if i == n-1 {
			if a[3][i] < 5 {
				res += "PRRRRUUUQLLLLDDDD"
			} else if a[3][i] < 10 {
				res += "PRRRRUUQLLLLDDD"
			} else if a[3][i] < 15 {
				res += "PRRRRUQLLLLDD"
			} else if a[3][i] < 20 {
				res += "PRRRRQLLLLD"
			} else {
				res += "PRRRRDQLLLL"
			}
		} else {
			if a[3][i] < 5 {
				res += "PRRRRUUUQLLLLDDD"
			} else if a[3][i] < 10 {
				res += "PRRRRUUQLLLLDD"
			} else if a[3][i] < 15 {
				res += "PRRRRUQLLLLD"
			} else if a[3][i] < 20 {
				res += "PRRRRQLLLL"
			} else {
				res += "PRRRRDQULLLL"
			}
		}
	}
	for i := 0; i < n; i++ {
		if i == n-1 {
			if a[4][i] < 5 {
				res += "PRRRRUUUUQ"
			} else if a[4][i] < 10 {
				res += "PRRRRUUUQ"
			} else if a[4][i] < 15 {
				res += "PRRRRUUQ"
			} else if a[4][i] < 20 {
				res += "PRRRRUQ"
			} else {
				res += "PRRRRQ"
			}
		} else {
			if a[4][i] < 5 {
				res += "PRRRRUUUUQLLLLDDDD"
			} else if a[4][i] < 10 {
				res += "PRRRRUUUQLLLLDDD"
			} else if a[4][i] < 15 {
				res += "PRRRRUUQLLLLDD"
			} else if a[4][i] < 20 {
				res += "PRRRRUQLLLLD"
			} else {
				res += "PRRRRQLLLL"
			}
		}
	}
	for i := 0; i < n; i++ {
		if i == 0 {
			fmt.Println(res)
		} else {
			fmt.Println("B")
		}
	}
}

func input(lines []string) (int, [][]int) {
	n, _ := strconv.Atoi(lines[0])
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		a[i] = make([]int, n)
		for j, s := range strings.Split(lines[i+1], " ") {
			a[i][j], _ = strconv.Atoi(s)
		}
	}

	return n, a
}

func getStdin() []string {
	stdin, _ := io.ReadAll(os.Stdin)
	return strings.Split(strings.TrimRight(string(stdin), "\n"), "\n")
}
