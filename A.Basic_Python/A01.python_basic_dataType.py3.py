'''
Python Basic(1)
: Data Types

By Daeho Jin
'''

### Part1: Data Types
print("\n*** Data Types ***")

### Integer and float numbers
print("\n1. Integer and float numbers")
a=17
b=7
print("a = {}:\ttype = {}".format(a,type(a)))
print("b = {}:\ttype = {}".format(b,type(b)))
print("c = a/b")
c=a/b
print("c = {}:\ttype = {}".format(c,type(c)))
print("---> Division by integer results in float type\n")
print("d = a//b")
d=a//b
print("d = {}:\ttype = {}".format(d,type(d)))
input("\nPress Enter to continue...\n")
print("----------------------------------------\n")

### Print format
print("\n2. Print format examples")
format_test = '{},\t{:d},\t{:02d},\t{:03d},\t{:.2f},\t{:.3f}'
print(format_test)
print(format_test.format(a,a,a,a,a,c))
format_test2 = '{1:d},\t{2:.2f},\t{0:.1f}'
print('\n'+format_test2)
print(format_test2.format(a,b,c))
print("\nHow about multi-lines? Use tripple quote mark!")
multi_lines='''
Hello, my name is {name}.
I am {age:d} years old.
My favorite food is {food}
'''
keywords={"name":"Bob", "age":35, "food":"chococake"}  # This is dictionry!
print(multi_lines.format(**keywords))  # two stars: distribute items of "key:value"
input("\nPress Enter to continue...\n")
print("----------------------------------------\n")

### String
print("\n3. String examples")
print("d = str(c) # Change type from float to string ")
d=str(c)
print("d = {}:\ttype = {}".format(d,type(d)))
print("len(d), d[0:4], d[-3:]")
print("{}, {}, {}".format(len(d),d[0:4],d[-3:]))
print("c+c vs. d+d vs. d*2")
print("{} vs. {} vs. {}".format(c+c,d+d,d*2))
print("len(d*2)")
print(len(d*2))
input("\nPress Enter to continue...\n")
print("----------------------------------------\n")

### Printing unicode
print("\n4. Unicode example")
print("El Ni\u00F1o and La Ni\u00F1a")
print("Delta: {}, epsilon: {}, degree: {}".format('\u0394','\u03B5','\u00B0'))
input("\nPress Enter to continue...\n")
print("----------------------------------------\n")

### Boolean
print("\n5. Boolean type")
print("boo1, boo2 = True, False")
boo1, boo2 = True, False
print("boo1 = {}:\ttype = {}".format(boo1,type(boo1)))
print("Value of {} and {}:".format(boo1,boo2))
print(int(boo1),int(boo2))
print("{}+{} = {}".format(boo1,boo2,boo1+boo2))
print("{} and {} = {}".format(boo1,boo2,boo1 and boo2))
print("bool(-1) = {}, bool(0) = {}, bool(1) = {}, bool(2) = {}".format(bool(-1),bool(0),bool(1),bool(2)))
print("bool(-0.1) = {}, bool(0.) = {}, bool(0.1) = {}".format(bool(-0.1),bool(0.),bool(0.1)))
print("---> Value zero(0) is False, and all others are True")
input("\nPress Enter to continue...\n")

print("THE END: Python Basic(1) - Data Types\n")
