class Car:
    Model = input("Введите модель автомобиля: ")
    Release = input("Введите год выпуска автомобиля: ")
    Engine = input("Введите объем двигателя: ")
    Color = input("Введите цвет автомобиля: ")
    Prise = input("Введите цену автомобиля: ")

    if __name__ == "__main__":
        allowed_options = "Model/Release/Engine/Color/Prise/exit"

        while True:
            desision = input(f"What should I do?{allowed_options}: ")
            if desision == "Model":
                print(Model)
            elif desision == "Release":
                print(Release)
            elif desision == "Engine":
                print(Engine)
            elif desision == "Color":
                print(color)
            elif desision == "Prise":
                print(Prise)
            elif desision == "exit":
                print("Exiting..")
                break
            else:
                print(f"Пожалуйста используйте разрешенные варианты. {allowed_options}")

