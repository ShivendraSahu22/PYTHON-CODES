// Write a program to print all three-digit numbers in Which any two or all three digit are the same

for num in range (100,1000)
temp=num
a = num // 100
b = (num // 10) % 10
b = num % 10
if a == b or b == c or c == a:
  print(num)
