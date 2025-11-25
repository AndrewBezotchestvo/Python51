# Проверка корректности e-mail
# Создай класс EmailValidator со статическим методом
# is_valid(email), который возвращает True, если в
# строке есть символ '@' и хотя бы одна точка после него.
#  Проверку реализовать без использования регулярных
#  выражений.

class EmailValidator:
    __email_variants = ["@mail.ru", "@yandex.ru", "@gmail.com", "@inbox.com"]
    @staticmethod
    def is_valid(email):
        valid = False
        for variant in EmailValidator.__email_variants:
            if email.endswith(variant):
                valid = True
                break
        return valid

print(EmailValidator.is_valid("выаль@gmail.com"))

