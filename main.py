from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('test_template.html')
# Task1
myname = "color"
mystring = "синий зеленый красный"
mylist = [1, 2]

# Task2
books = [
    {"title": "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title": "Белая гвардия",
     "author": "Булгаков М.А.",
     "price": 600.00},
    {"title": "Война и мир",
     "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title": "Анна Каренина",
     "author": "Толстой Л.Н.",
     "price": 450.10},
    {"title": "Игрок",
     "author": "Достоевский Ф.М.",
     "price": 234.55}
]
n = 3

result_html = template.render(name=myname, string=mystring, list=mylist, books=books, count=n)
# создадим файл для HTML-страницы
f = open('test_rezult.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
