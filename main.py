#Ways to print even numbers from 1-100

#1
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

#2
even_numbers = [print(x) for x in range(1,101) if x % 2 == 0]