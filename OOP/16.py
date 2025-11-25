# Конвертер температур
# Создай класс TemperatureConverter со следующими статическими методами:
# c_to_f(celsius) — конвертация °C → °F
# f_to_c(fahrenheit) — конвертация °F → °C
# Класс должен иметь статический атрибут precision —
# количество знаков после запятой при округлении результата.

class TemperatureConverter:
    precision = 6
    @classmethod
    def c_to_f(cls, celsius):
        result = round(celsius * 9 / 5 + 32, cls.precision)
        return result

    @staticmethod
    def f_to_c(fahrenheit):
        result = round((fahrenheit - 32) * 5/9 , TemperatureConverter.precision)
        return result

print(TemperatureConverter.c_to_f(55))
print(TemperatureConverter.f_to_c(21))
