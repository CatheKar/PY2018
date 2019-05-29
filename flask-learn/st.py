from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/main/', methods = ['GET'])
def main():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')

    result = ""
    if None in (a, b, c):
        result = "Не введены данные"
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        D = b ** 2 - 4 * a * c
        if D < 0:
            result = "Дискриминант меньше 0"
        else:
            x1 = (-b + D ** 0.5) / 2
            x2 = (-b - D ** 0.5) / 2
            result = "x1 = " + str(x1) + ", x2 = " + str(x2)

    return render_template('mane.html', res=result)


