from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def root():
    return "This is root page"

if __name__ == "__main__":
    app.run()