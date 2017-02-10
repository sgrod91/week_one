import sys
size = int(raw_input('Size of square? '))

for i in range(size):
    print '*' * size

# alternate way to make a row of stars with a for loop
# for i in range(size):
#     for i in range(size):
#         sys.stdout.write('*')
#     print ''
