from flask import Flask, render_template, make_response, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))
    if not secret_number:
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))

    return response


@app.route("/result", methods=["POST"])
def result():
    secret_number = request.cookies.get("secret_number")
    guess = request.form.get("guess")

    if secret_number == guess:
        message = f"Congrats! The secret number was {secret_number}."
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif secret_number < guess:
        message = "False.. Try again and guess smaller!"
        return render_template("result.html", message=message)
    elif secret_number > guess:
        message = "False.. Try again and guess higher!"
        return render_template("result.html", message=message)


if __name__ == "__main__":
    app.run(use_reloader=True)
