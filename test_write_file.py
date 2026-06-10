from functions.write_file import write_file

result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result)

result1 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result1)

result2 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result2)