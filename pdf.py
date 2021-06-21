import pikepdf

file = open("wordlist.txt")

for password in file:
    try:
        with pikepdf.open("Chapter 1_Introduction to OS_2.pdf", password.strip()) as pdf:
            print("your pass word is found")
            print(password)
            break
    except:
        print("not found")
        continue
