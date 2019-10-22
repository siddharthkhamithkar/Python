num = int(input("Enter a number greater than 1000: "))
tnum = num
reverse = 0
while tnum:
    digit = tnum % 10
    tnum = tnum // 10
    reverse = reverse * 10 + digit
print("Reverse of", num, "is", reverse)
