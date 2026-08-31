from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "Flask API is running"}


@app.get("/hello")
def hello():
    return {"message": "Hello from the GET endpoint!"}


@app.post("/greet")
def greet():
    data = request.get_json(silent=True) or {}
    username = data.get("username")

    if not username:
        return {"error": "username is required"}, 400

    return {
        "message": f"Hello, {username}! Welcome to my Flask API."
    }


if __name__ == "__main__":
    app.run(debug=True)