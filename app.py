from flask import Flask, render_template, request

import Parser

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['GET', 'POST'])
def search():
    seachInformation = Parser.getInformation().search(request.form.get('searchINN'))#inn i do not know
    if seachInformation.__class__ is str:  # возвращаем мы строку, если ошибка произошла, эта функция проверит, состоит ли строка из букв и цифр
        message = ''

        if 'Page unavailable' in seachInformation:
            message = 'Страница недоступна! \n Повторите ввод или откройте сайт для поиска в браузере'#Стоит защита от запросов с одного ip, нужно будет открыть сайт и подтвердить что ты не робот
        elif 'Not Found.' in seachInformation:
            message = 'Сайт для запроса нелоступен 404'
        elif 'Error in get date.' in seachInformation:
            message = 'Проверьте правильность введенных данных!'

        return render_template('home.html', message=message)
    else:
        return render_template('home.html', information=seachInformation)


if __name__ == '__main__':
    app.run()
