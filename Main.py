print("Program Konversi Suhu")


# fungsi konversi celcius ke reamur, fahrenheit, dan kelvin
def konversiCelcius(celcius):
    # reamur
    reamur = (4 / 5) * celcius
    print(celcius, " Celcius = ", reamur, " Reamur")

    # fahrenheit
    fahrenheit = ((9 / 5) * celcius) + 32
    print(celcius, " Celcius = ", fahrenheit, " Fahrenheit")

    # kelvin
    kelvin = celcius + 273
    print(celcius, " Celcius = ", kelvin, " Kelvin")


# fungsi konversi reamur ke celcius, fahreinhet dan kelvin
def konversiReamur(reamur):
    # celcius
    celcius = (5/4) * reamur
    print(reamur, " Reamur = ", celcius, " Celcius")

    # fahrenheit
    fahrenheit = ((9/4) * reamur) + 32
    print(reamur, " Reamur = ", fahrenheit, " Fahrenheit")

    # kelvin
    kelvin = ((5/4) * reamur) + 273
    print(reamur, " Reamur = ", kelvin, " Kelvin")


# fungsi konversi fahrenheit ke celcius, reamur dan kelvin
def konversiFahrenheit(fahrenheit):
    # celcius
    celcius = ((5/9) * (fahrenheit - 32))
    print(fahrenheit, " Fahrenheit = ", celcius, " Celcius")

    # reamur
    reamur = ((4/9) * (fahrenheit - 32))
    print(fahrenheit, " Fahrenheit = ", reamur, " Reamur")

    # kelvin
    kelvin = (5/9) * (fahrenheit - 32) + 273
    print(fahrenheit, " Fahrenheit = ", kelvin, " Kelvin")


# fungsi konversi kelvin ke celcius, reamur dan fahrenheit
def konversiKelvin(kelvin):
    # celcius
    celcius = kelvin - 273
    print(kelvin, " Kelvin = ", celcius, " Celcius")

    # reamur
    reamur = ((4/5)*(kelvin-273))
    print(kelvin, " Kelvin = ", reamur, " Reamur")

    # fahrenheit
    fahrenheit = (9/5)*(kelvin-273) + 32
    print(kelvin, " Kelvin = ", fahrenheit, " Fahrenheit")
