#!/usr/bin/ruby

#  * A key-value pair [543121, 100] to the ` hackerrank ` object using ` store `
#  * Retain all key-value pairs where keys are Integers ( clue : is_a? Integer ) 
#  * Delete all key-value pairs where keys are even-valued. 

hackerrank.store(543121,100)
hackerrank.each do | k,v |
    hackerrank.delete(k) if not k.is_a? Integer
    hackerrank.delete(k) if k % 2 == 0
end
