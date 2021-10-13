with open('words.txt', 'r') as file:

    temp = file.readlines()
    words = temp.split()
    for i in words:
        if "c" in i:
            print(i.strip(',.'))
