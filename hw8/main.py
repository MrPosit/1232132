import re

'''Задание №1.
Напишите программу, в которой возвращаются домены из списка e-mail адресов.
'''

def extract_domains(emails):
    domain_pattern = r'@([a-zA-Z0-9.-]+)'
    domains = re.findall(domain_pattern, emails)
    return domains

emails = "user1@example.com, user2@domain.com, user3@test.net"
domains = extract_domains(emails)
print(domains)


'''Задание №2.
Напишите программу, в которой извлекаются слова, начинающиеся на гласную букву.
'''

def extract_vowel_words(text):
    vowel_pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
    vowel_words = re.findall(vowel_pattern, text)
    return vowel_words

text = "Apple banana orange pear grape"
vowel_words = extract_vowel_words(text)
print(vowel_words)



'''Задание №3.
Напишите программу, в которой разбивается строка по нескольким разделителям
'''

def split_by_multiple_delimiters(text, delimiters):
    delimiters_regex = '|'.join(map(re.escape, delimiters))
    parts = re.split(delimiters_regex, text)
    return parts

text = "apple,banana;orange grape|pear"
delimiters = [',', ';', ' ', '|']
parts = split_by_multiple_delimiters(text, delimiters)
print(parts)
