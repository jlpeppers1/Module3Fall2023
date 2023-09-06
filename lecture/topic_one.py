#Sequential
print('This is sequential')
conditional = False

#conditional
if (conditional):
    #statements below here
    print('We are in the if branch') #if branch
#else if
elif(not conditional):
    print('We are in the else if')
else:
    print('We are in the else branch') #else branch

#Back to sequential
print('This always happens since it is not indented')

# just if
# if else
# if elif elif...
# if elif ... else

#chaining (connecting patterns)

age = 4
movie = 'r'
if (age < 17 and age > 10 and movie == 'r'):
    print('age below 17')

print(f"Age < 17 becomes:\t{age < 17}")
less_than_17 = age < 17
print(f"Age > 10 becomes:\t{age > 10}")
greater_than_10 = age > 10
print(f"movie == 'r' becomes:\t{movie == 'r'}")
movie_is_rated_r = movie == 'r'

print(f"age in range:\t{less_than_17 and greater_than_10}")
in_range = less_than_17 and greater_than_10
print(f"in_range and r rated:\t{in_range and movie_is_rated_r}")

#build upon that

if (age < 17 and age > 10 and movie == 'r'):
    print('R rated movies age 11-16 must accompanied by an adult')
elif (age >= 17):
    print("Enjoy the movie")
else:
    print("You cannot come into the movie")
