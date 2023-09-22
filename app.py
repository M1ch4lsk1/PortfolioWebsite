from flask import Flask, render_template
from flask import url_for
app = Flask(__name__, template_folder="src/templates",
            static_folder="src/static")


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
