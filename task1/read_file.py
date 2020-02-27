try:
    file= open('text.txt', 'r')
    arrayOfStrings = file.readlines()
    for strings in arrayOfStrings:
        print(strings, end="")
    file.close()
except Exception as e:
    print(e)
