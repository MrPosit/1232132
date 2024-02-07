'''1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}'''
# original_list_1 = [1, 2, 3, 4, 5, 6, 7]
# result_dict_1 = {x: x**3 for x in original_list_1 if x % 2 != 0}
# print(result_dict_1)

'''2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}'''
# original_list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# result_set_2 = {x for x in original_list_2 if x % 2 == 0}
# print(result_set_2)


'''3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного'''
# step = 10
# n = 100
# result_list_3 = [i for i in range(0, n, step)]
# print(result_list_3)

'''4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7,
в диапазоне от 0 до n.'''
# def generator_divisible_by_seven(n):
#     for i in range(n + 1):
#         if i % 7 == 0:
#             yield i

# n_value = 50
# for num in generator_divisible_by_seven(n_value):
#     print(num)


'''На вход полается последовательность символов (символы могут быть любыми, в том
числе и не буквенными, могут повторяться). Выведите все слова, которые можно составить
из букв данной последовательности и их количество. Если в последовательности буква
повторяется, то и в словах она может повторяться, но количество повторений в слове должно
быть не более количества повторений в последовательности. Если в последовательности
буква встречается 1 раз, то и в словах буква может встречаться не более 1 раза.
Слова должны выводиться в порядке возрастания длины, в последовательности не
должно быть двух одинаковых слов.
Помните, что в словах позиция буквы имеет значение, т.е. слова dog и god – 2 разных
слова. Воспользуйтесь средствами модуля itertools.
'''
def generate_words(input_str):
    result_words = set()
    count = {}

    for char in input_str:
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    def generate(word, count):
        if word:
            result_words.add(word)

        for char in count:
            if count[char] > 0:
                count[char] -= 1
                generate(word + char, count)
                count[char] += 1

    generate('', count)
    result_words.add("8")
    sorted_words = sorted(result_words, key=lambda x: (len(x), x))
    return sorted_words

input = "k98.ok"
result = generate_words(input)
for word in result:
    print(word)
