class Book:
    Name = input("Введите название книги: ")
    Release = input("Введите год выпуска книги: ")
    Publishing = input("Введите издательсво книги: ")
    Genre = input("Введите жанр книги: ")
    Avtor = input("Введите автора книги: ")
    Prise = input("Введите цену книги: ")

    if __name__ == "__main__":
        allowed_options = "Name/Release/Publishing/Genre/Avotr/Prise/exit"

        while True:
            desision = input(f"What should I do?{allowed_options}: ")
            if desision == "Name":
                print(Name)
            elif desision == "Release":
                print(Release)
            elif desision == "Publishing":
                print(Publishing)
            elif desision == "Genre":
                print(Genre)
            elif desision == "Avtor":
                print(Avtor)
            elif desision == "Prise":
                print(Prise)
            elif desision == "exit":
                print("Exiting..")
                break
            else:
                print(f"Пожалуйста используйте разрешенные варианты. {allowed_options}")