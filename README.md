# HackerRank
My personal Repo for HackerRank stuff

I put an alias to hr in `.bashrc` as to auto change directory when run in a shell.
```
hr() {
    cd "$(${HOME}/repos/HackerRank/hrdownload.py "$1")"
}

```

example usage:

```
hr https://www.hackerrank.com/challenges/simple-array-sum/problem
```
