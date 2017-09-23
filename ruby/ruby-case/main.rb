#!/usr/bin/ruby
def identify_class(obj)
    case obj
    when Hacker
        v = "It's a Hacker!" 
    when Submission
        v= "It's a Submission!" 
    when TestCase 
        v = "It's a TestCase!" 
    when Contest 
        v =  "It's a Contest!" 
    else
        v = "It's an unknown model" 
    end
    puts v
end
