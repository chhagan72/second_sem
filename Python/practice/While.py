# while loops
# With the while loop we can execute a set of statements as long as a condition is true.

i =2
while i < 6:
    print(i)
    i+=1


# break Statement
# With the break statement we can stop the loop even if the while condition is true:
a =3
while a>10:
    print(i)
    if a == 3:
        print("a Or 3 are equal")
        break
    i += 1

# continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
a =3
while a>10:
    i += 1
    if a == 3:
        print("a Or 3 are equal")
        continue
    print(i)