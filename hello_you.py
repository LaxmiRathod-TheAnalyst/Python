#Ask user for name
name = input("What is your name?: ")
print(name)

#Ask user for age
age = input("How old are you?: ")
print(age)

print(type(name))
print(type(age))

#Ask user for city
city = input("What city do you live in?: ")
print(city)

#Ask user what they enjoy
love = input("What do you love doing?: ")
print(love)

#create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name,age,city,love)



#print output to screen
print(output)
