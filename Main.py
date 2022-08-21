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
