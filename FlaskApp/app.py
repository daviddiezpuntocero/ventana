from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Hola Mundo"

if __name__ == "__main__":