from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])




if __name__ == '__main__':
    app.run(debug=True)