from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Главная страница"

@app.route('/userlist')
def userlist():
    return "Пользователи"

@app.route('/contacts')
def contacts():
    return "Контакты"


if __name__=="__main__":
    app.run(debug=True)



