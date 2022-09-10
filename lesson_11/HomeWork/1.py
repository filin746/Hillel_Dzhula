name: str = input ("Введите название файла: ")
f = open (name, "r")

allowed_options = 'Выберите один из вариантов: a/b/c/d/e/f: '
v = input(f"{allowed_options}")

if v == 'a':
    fd = f.readlines()
    print(fd[8])

elif v == "b":
    fd = f.readlines()
    print(fd[0])
elif v == "c":
    print(*f)
#elif v == "d":

elif v == "e":
    count = sum(1 for _ in f)
    print(count)

elif v == "f":
     print("Exiting..")
    #break
else:
    print(f"Пожалуйста используйте разрешенные варианты. {allowed_options}")


