from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

@app.route("/kursus")
def kursus():
    return render_template("kursus.html")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

if __name__ == "__main__":
    app.run(debug=True)
