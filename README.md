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

output files: (python is the default language configured in the hrdownload.py script)
```
repos/HackerRank/python/simple-array-sum/challenge_sample_input
repos/HackerRank/python/simple-array-sum/challenge_sample_output
repos/HackerRank/python/simple-array-sum/main.pyc
repos/HackerRank/python/simple-array-sum/content
repos/HackerRank/python/simple-array-sum/main.py
```
