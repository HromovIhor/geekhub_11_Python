"""6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя"""

def function(string):
    string_lenth = len(string)
    letters = sum(i.isalpha() for i in string)
    digits = sum(i.isdigit()for i in string)
    if 30 <= string_lenth <= 50:
        print("The length of string is:", string_lenth)
        print("The number of 'letters' in the string is:", letters)
        print("The number of 'digits' in the string is:", digits)
    elif  string_lenth <= 30:
        string_with_no_digits = ''
        sum_of_all_digits = 0
        for i in string:
            if i.isdigit():
                sum_of_all_digits += int(i)
            elif i.isalpha():
                string_with_no_digits += i
        print("Sum of all the digits in the string is: {}\nString without digits is - '{}'".format(sum_of_all_digits, string_with_no_digits))
    else:
        for i in range(len(long_user_string)):
            print("The Character at %d Index Position = %c" %(i, long_user_string[i]))

long_user_string = input("Enter a looong string like this ex. 'f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345':\n")
function(long_user_string)
