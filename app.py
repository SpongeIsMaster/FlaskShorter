from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

short_url = ''
links = []
id = 0

@app.route("/", methods=["POST", "GET"])
def home():
    global link, links, id, short_url
    if request.method == "POST":
        id = id + 1
        links.append((id, request.form["long-url"]))
        short_url = f"http://127.0.0.1:5000/shortener/{id}"
        return redirect(url_for("succes"))
    else:
        return render_template("towrite.html")

@app.route("/succes")
def succes():
    global short_url
    print(links)
    return render_template("succes.html", link = short_url)

@app.route("/shortener/<id>")
def findAress(id):
    return redirect(links[int(id) - 1][1])

if __name__ == "__main__":
    app.run(debug=True)