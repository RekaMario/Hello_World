# 1. TASK: print "Hello World"
import numbers


print("Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello"  , name )	# with a comma
print( "Hello" + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
numb = 42
print("Hello" , numb )	# with a comma
print("Hello" + str(numb) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I Love to eat {}  and  {}.".format(fave_food1, fave_food2 ) ) # with .format()
print(f"I Love to eat {fave_food1}  and {fave_food2}.") # with an f string

