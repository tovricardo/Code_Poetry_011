poem = "A car, a man, a maraca\nA car, a man, a maraca\nA car, a man, a maraca\ncar, a man, a maraca\ncar, a man, a maraca\ncar, a man, a maraca\na maraca\na maraca\na mrc\nmrc\n mrc\nmrc\nmärc\nmärc\nmɑrc\nmɑrc\nmɒrc\nmɒrc"
count = 0
while (count is not 3):
    for index in range(0, len(poem)):
        if (count is 0):
            print(poem[index])
            new_poem = poem
        if (count is 1):
            if (poem[index] is 'a'):
                new_poem += 'u'
                print("o")
            else:
                new_poem += poem[index]
                print(poem[index])
        if (count is 2):
            if (poem[index] is 'ä'):
                new_poem += 'i'
                print("i")
            else:
                new_poem += poem[index]
                print(poem[index])
    print(new_poem)
    new_poem = ""
    count += 1
