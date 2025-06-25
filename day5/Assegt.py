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
'''The above question is not '''
binary = 1101  # example binary number
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

print("Decimal:", decimal)

