test_file = open('test.txt','r')

print(test_file.readable())
# print(test_file.readline()) # returns first line of file

# print(test_file.readlines()) # returns list 


# Using loop
for lines in test_file.readlines():
    print(lines)

test_file.close()
