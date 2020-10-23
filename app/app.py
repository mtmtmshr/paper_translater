from flask import Flask,render_template, redirect, request
from app.process_sentence import process_sentence

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        text = request.form["text"]
        processed_text = process_sentence(text)
        return redirect("https://www.deepl.com/translator#en/ja/{}".format(processed_text))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
