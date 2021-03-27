'''Please write a program that print the first N prime numbers.
N should be declared as a variable at the beginning.
You can hand it in as a link to your file at github or as a file directly.

Definition: a prime number refers to a natural number that has no other factors except 1
and itself among the natural numbers greater than 1.'''

def prime(count, n):
    for i in range(2, n-1):
        if n % i ==0:  #% if the reminder is equal to zero.
            return count
        else:
            continue
    print(str(n))
    count += 1  #count=count+1
    return count
print("Hello, please enter an nature number: ")
N = int(input())
s = 2 # the starting number
times = 0
if N <= 0:
    print("Oh no! Please enter an positive nature number")
else:
    print("Your entered " + str(N) + '. First ' + str(N) + 'prime number are:' )
    while True:
        times = prime(times, s)
        s+=1
        if times ==N:
            break
