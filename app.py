from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

end_link = ""

@app.route("/", methods=["POST", "GET"])
def elo():
    return render_template("towrite.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    global end_link
    if request.method == "POST":
        link = request.form["long-url"]
        end_link = link
        return redirect(url_for("succes"))
    else:
        return render_template("towrite.html")

@app.route("/succes")
def succes():
    global end_link
    print(end_link)
    return render_template("succes.html")
    
if __name__ == "__main__":
    app.run(debug=True)