#!/usr/bin/ruby

5
1 2 3
2 1 3
3 2 5
3 3 3
1 2 5

def fun(a,b,c)
    return a.range?(b,c)
end

print fun(5,1,6)

