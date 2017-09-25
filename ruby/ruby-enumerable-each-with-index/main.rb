#!/usr/bin/ruby
def skip_animals(animals, skip)
    return animals if not animals.count > skip
    print animals," ",skip,"\n"
    a = Array.new
    animals.each_with_index { | item, index |
        if index >= skip 
           print "anicnt: ",animals.count," a:cnt ",a.count," skip: ",skip," idx: ",index,"\n"
           a.push("#{index}:#{item}") 
        end
    }
    return a
end

puts skip_animals(["bat", "cow", "jaguar", "panda", "tiger", "deer"],2)
puts skip_animals(["leopard", "bear", "fox", "wolf", "dog", "cat"],0)
