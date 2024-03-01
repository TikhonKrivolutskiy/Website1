from flask import Flask, url_for, request
 
app = Flask(__name__)
 
@app.route('/')
def title():
    return "Миссия Колонизация Марса"
 
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
 
@app.route('/promotion')
def promotion():
    list1 = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!"]
    return "</br>".join(list1)
 
@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars1.png"></img>
                    <h4>Вот она какая, красная планета.</h4>
                  </body>
                </html>"""
 
@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars1.png')}"></img>
                    <h4><div class="alert alert-dark" role="alert">Человечество вырастает из детства.</div></h4>
                    <h4><div class="alert alert-success" role="alert">Человечеству мала одна планета.</div></h4>
                    <h4><div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div></h4>
                    <h4><div class="alert alert-warning" role="alert">И начнем с Марса!</div></h4>
                    <h4><div class="alert alert-danger" role="alert">Присоединяйся!</div></h4>
                  </body>
                </html>'''
 
@app.route('/astronaut_selection')
def astronaut_selection():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="1" value="1">
                                          <label class="form-check-label" for="1">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="2" value="2">
                                          <label class="form-check-label" for="2">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="3" value="3">
                                          <label class="form-check-label" for="3">Строитель</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="4" value="4">
                                          <label class="form-check-label" for="4">Экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="5" value="5">
                                          <label class="form-check-label" for="5">Врач</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="6" value="6">
                                          <label class="form-check-label" for="6">Инженер по терраформированию</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="7" value="7">
                                          <label class="form-check-label" for="7">Климатолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="8" value="8">
                                          <label class="form-check-label" for="8">Специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="9" value="9">
                                          <label class="form-check-label" for="9">Астрогеолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="10" value="10">
                                          <label class="form-check-label" for="10">Гляциолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="11" value="11">
                                          <label class="form-check-label" for="11">Инженер жизнеобеспечения</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="12" value="12">
                                          <label class="form-check-label" for="12">Метеоролог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="13" value="13">
                                          <label class="form-check-label" for="13">Оператор марсохода</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="14" value="14">
                                          <label class="form-check-label" for="14">Киберинженер</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="15" value="15">
                                          <label class="form-check-label" for="15">Штурман</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="occupation" id="16" value="16">
                                          <label class="form-check-label" for="16">Пилот дронов</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять учасие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="4" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="accept" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h4>Эта планета близка к земле;</h4>
                    <h4><div class="alert alert-success" role="alert">На ней много необходимых ресурсов;</div></h4>
                    <h4><div class="alert alert-dark" role="alert">На ней есть вода и атмосфера;</div></h4>
                    <h4><div class="alert alert-warning" role="alert">На ней есть небольшое магнитное поле;</div></h4>
                    <h4><div class="alert alert-danger" role="alert">Наконец, она просто красива!</div></h4>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h4>Претендент на участие в миссии {nickname}:</h4>
                    <h4><div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div></h4>
                    <h4>составляет {rating}!</h4>
                    <h4><div class="alert alert-warning" role="alert">Желаем удачи!</div></h4>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h2>для участия в миссии</h2>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h2>для участия в миссии</h2>
                            <form method="post" enctype="multipart/form-data">
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="static/img/{f.filename}"></img>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')