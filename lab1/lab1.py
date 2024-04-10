def caeser(k, realText):
    up = "abcdefghijklmnopqrstuvwxyz"
    k2 = ""
    outLetter = ""

    for eachLetter in realText:
        if eachLetter.isalpha() or eachLetter.isnumeric():
            index = up.index(eachLetter)
            crypting = (index + k) % len(up)
            newLetter = up[crypting]
        elif eachLetter in a:
            index = a.index(eachLetter)
            crypting = (index + k) % len(a)
            newLetter = a[crypting]
        else:
            newLetter = eachLetter

        outLetter += newLetter

    return outLetter

def affina(k, realText):
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    up += "abcdefghijklmnopqrstuvwxyz"
    up += "0123456789"
    a = "!@#$%^&*()_+<>?"

    outLetter = ""

    for eachLetter in realText:
        if eachLetter.isalpha() or eachLetter.isnumeric():
            index = up.index(eachLetter)
            crypting = (index * k) % len(up)
            newLetter = up[crypting]
        elif eachLetter in a:
            index = a.index(eachLetter)
            crypting = (index * k) % len(a)
            newLetter = a[crypting]
        else:
            newLetter = eachLetter

        outLetter += newLetter

    return outLetter

def ship(k):
    for x in range(62):
        if (k * x) % 62 == 1:
            return x
    return None

file1 = open("myfile.txt", "r")
realText = file1.read()
file1.close()

print("Enter a value for k:")
k = int(input())

file1 = open("MyFile1.txt", "w")
file1.write(caeser(k, realText))
file1.close()

file1 = open("MyFile2.txt", "w")
file1.write(affina(k, realText))
file1.close()

print(ship(k))
print(realText)

file1 = open("MyFile3.txt", "w")
file1.write(affina(ship(k), affina(k, realText)))
file1.close()
