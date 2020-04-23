from flask import Flask, render_template
import os
import random

app = Flask(__name__)
# list of dog images
images = [
    "giphy.gif",
    "giphy01.gif",
    "giphy02.gif",
    "giphy03.gif",
    "giphy04.gif",
    "giphy05.gif",
    "giphy06.gif",
    #"giphy07.gif",
    "giphy08.gif",
    "giphy09.gif",
    "giphy10.gif",
    "giphy11.gif",
    "giphy12.gif",
    "giphy13.gif",
    "giphy14.gif",
    "giphy15.gif",
    "giphy16.gif",
    "giphy17.gif",
    "giphy18.gif",
    "giphy19.gif",
    "giphy20.gif",
    "R9V7tnR.gif",
    "R9V8tnz.gif",
    "S9V7tna.gif",
    "ride.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
