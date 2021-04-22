import os
import shutil

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploadLabel', methods=['POST'])
def uploadLabel():
    file = request.files.get('file')
    print(file)
    print(file.filename)

    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    file.save("./tmp/" + file.filename)
    return {'message': 'success'}


if __name__ == '__main__':
    app.run()
