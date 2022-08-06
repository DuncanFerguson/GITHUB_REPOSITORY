# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('first_app.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('first_app.html')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

    