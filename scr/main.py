from flask import Flask
from jinja2 import FileSystemLoader, Environment
import requests

app = Flask(__name__)


@app.route('/')
def index():
    img = requests.get("https://picsum.photos/350")

    paginas = FileSystemLoader('templates')
    env = Environment(loader=paginas)
    index = env.get_template('index.html')

    return index.render(imagem='https://picsum.photos/350')


if __name__ == "__main__":
    app.run(debug=False, port=5000)
