'''print the binary value of 12'''

'''n = 12
binary = ""

while n > 0:
    temp = n % 2
    binary = str(temp) + binary  # add to front
    n = n // 2


print(binary)  # Output: 01100'''

'''using for loop '''
'''n = 12
binary = ""

while n > 0:
    temp = n % 2
    binary = str(temp) + binary  # add to front
    n = n // 2

# Optional: pad with leading zeros (e.g., to make it 5 bits)
binary = binary.zfill(5)

print(binary)  # Output: 01100'''


'''Write a program to convert a binary number into a decimal number'''
'''The above question is not to do using only for and while loop '''
'''binary = 1101  # example binary number
decimal = 0
power = 0

# First, count number of digits in binary
temp = binary
count = 0
while temp > 0:
    count += 1
    temp = temp // 10

# Process each digit from right to left
for i in range(count):
    digit = binary % 10
    decimal = decimal + digit * (2 ** i)
    binary = binary // 10

print("Decimal:", decimal)'''

#different approach is there

'''binary = 1011
decimal = 0
power = 0
while binary > 0:
    digit = binary % 10
    decimal += digit * (1 << power)   # use bit-shift instead of (2 ** power)
    power += 1
    binary //= 10
print(decimal)'''

#Python in-built shortcut (not pure DSA, but handy)

'''binary = "1011"
decimal = int(binary, 2)
print(decimal)  # 11'''





