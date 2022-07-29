class Stadium:
    Name = input("Введите название стадиона: ")
    Date = input("Введите дату открытия стадиона: ")
    Country = input("Введите страну в котором стадион: ")
    City = input("Введите город в котором стадион: ")
    Location = input("Введите размещение стадиона: ")

    if __name__ == "__main__":
        allowed_options = "Name/Date/Country/City/Location/exit"

        while True:
            desision = input(f"What should I do?{allowed_options}: ")
            if desision == "Name":
                print(Name)
            elif desision == "Date":
                print(Date)
            elif desision == "Country":
                print(Country)
            elif desision == "City":
                print(City)
            elif desision == "Location":
                print(Location)
            elif desision == "exit":
                print("Exiting..")
                break
            else:
                print(f"Пожалуйста используйте разрешенные варианты. {allowed_options}")