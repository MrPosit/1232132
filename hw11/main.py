'''а) Создайте json файл в операционной системе, заполните его данными с сайта
https://jsonplaceholder.typicode.com/todos/
б) Прочитайте этот файл в массив python-словарей.
в) Запишите каждый из этих словарей в отдельный json-файл.'''
import json
import requests

url = 'https://jsonplaceholder.typicode.com/todos/'
todos = requests.get(url).json()
data = json.loads(todos)

for idx, item in enumerate(data, start=1):
    with open(f'todo_{idx}.json', 'w') as file:
        json.dump(item, file, indent=4)






'''а) Создайте word файл в операционной системе, заполните его текстом «Hello Python».
б) Прочитайте этот файл, только жирный текст в python-строку и выведите на экран.
в) Создайте абзац с текстом и запишите это в новый word-файл, изменит шрифт и размер
шрифта.
'''

doc = Document()
doc.add_paragraph("Hello Python")
doc.save("hello.docx")

doc = Document("hello.docx")
bold_text = [p.text for p in doc.paragraphs if any(run.bold for run in p.runs)]
print(bold_text)

new_doc = Document()
paragraph = new_doc.add_paragraph("New paragraph with modified font.")
for run in paragraph.runs:
    run.font.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Arial'
new_doc.save("modified.docx")
