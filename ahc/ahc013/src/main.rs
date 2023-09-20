#![allow(non_snake_case, unused_macros)]
use rand::prelude::*;
use itertools::Itertools;

use std::collections::{HashMap, HashSet};

use proconio::{input, marker::*};
use rand::prelude::*;
use svg::node::{
    element::{Line, Rectangle, Text as TextElement, Title},
    Text, Value,
};

#[cfg(target_arch = "wasm32")]
use wasm_bindgen::prelude::*;

pub struct Result {
    moves: Vec<(usize, usize, usize, usize)>,
    connects: Vec<(usize, usize, usize, usize)>,
}

pub struct Solver {
    n: usize,
    k: usize,
    c: Vec<Vec<usize>>,
    lim: usize,
}

impl Solver {
    pub fn new(n: usize, k: usize, c: Vec<Vec<usize>>, lim: usize) -> Self {
        Solver {
            n: n, k: k, c: c, lim: lim
        }
    }

    // fn _move(&self, lim: usize) -> Vec<usize> {
    //     moves = [];

    // }
    fn _connect(&mut self, lim: usize) -> Vec<Vec<usize>>{
        let used: usize = 9;
        let vecs: [[isize; 2]; 4] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        let mut connects: Vec<Vec<usize>> = vec![vec![0; 0]; 0];

        let can_connect = |i: usize, j: usize, v: [usize; 2], c_tmp: &Vec<Vec<usize>>| {
            let mut i2: usize = i + v[0];
            let mut j2: usize = j + v[1];
            while i2 < self.n && j2 < self.n {
                if c_tmp[i2][j2] == 0 {
                    i2 += v[0];
                    j2 += v[1];
                    continue;
                }
                else if c_tmp[i2][j2] == c_tmp[i][j] {
                    return true;
                }
                return false;
            }
            false
        };
        let mut do_connect = |i: usize, j: usize, v: [usize; 2], c_tmp: &Vec<Vec<usize>>| {
            let mut i2 = i + v[0];
            let mut j2 = j + v[1];
            while i2 < self.n && j2 < self.n {
                if c_tmp[i2][j2] == 0 {
                    c_tmp[i2][j2] = used;
                } else if self.c[i2][j2] == self.c[3][j] {
                    connects.push(vec![i, j, i2, j2]);
                    return;
                } else {
                    println!("error");
                }
                i2 += v[0];
                j2 += v[1];
            }
        };
        for i in 0..self.n {
            for j in 0..self.n {
                if self.c[i][j] == 0 || self.c[i][j] == used {
                    continue;
                }
                for v in vec![[0, 1], [1, 0]] {
                    if can_connect(i, j, v, &self.c) {
                        do_connect(i, j, v, &self.c);
                        if connects.len() >= lim {
                            return connects;
                        }
                    }
                }
            }
        }
        connects
    }


}

#[derive(Clone, Debug)]
pub struct UnionFind {
    parents: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            parents: (0..n).into_iter().collect(),
            size: vec![1; n],
        }
    }

    pub fn find(&mut self, x: usize) -> usize {
        if self.parents[x] == x {
            x
        } else {
            self.parents[x] = self.find(self.parents[x]);
            self.parents[x]
        }
    }

    pub fn unite(&mut self, x: usize, y: usize) {
        let mut x = self.find(x);
        let mut y = self.find(y);
        if self.size[x] < self.size[y] {
            ::std::mem::swap(&mut x, &mut y);
        }
        if x != y {
            self.size[x] += self.size[y];
            self.parents[y] = x;
        }
    }

    pub fn same(&mut self, x: usize, y: usize) -> bool {
        self.find(x) == self.find(y)
    }
}

fn calc_score(n: u16, k: u16, c: u16, res: Result) {

}

fn print_answer(res: Result) {

}

fn main() {
}
