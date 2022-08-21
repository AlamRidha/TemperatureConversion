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
