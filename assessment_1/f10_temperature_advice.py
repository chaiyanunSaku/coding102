def temperature_advice(temperature: float) -> str:
    if temperature >= 35:
        return "Very hot, drink water"
    elif temperature >= 25:
        return "Warm weather"
    else:
        return "Cool weather"


print(temperature_advice(44))
print(temperature_advice(25))
print(temperature_advice(16))