file_to_make = open("bigfile.txt", "a")
while True:
    try:
        file_to_make.write("hello")
    except:
        file_to_make.close()
        break

