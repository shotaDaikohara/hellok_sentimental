from flask import *
from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer
model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
nlp = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def odd_even():
    if request.method == "GET":
        return """
        文章を入力してください。ネガティブかポジティプか判定します
        <form action="/" method="POST">
        <input name="str"></input>
        </form>"""
    else:
        try:
            return """
            入力された文章「{}」は{}です！　{}度は{}％。
            <form action="/" method="POST">
            <input name="str"></input>
            </form>""".format(request.form["str"],
                            nlp(request.form["str"])[0]["label"],
                            nlp(request.form["str"])[0]["label"],
                            round(nlp(request.form["str"])[0]["score"]*100,2))
        
        except:
            return """
                    エラーが発生しました。文章を変更してお試しください。
                    <form action="/" method="POST">
                    <input name="str"></input>
                    </form>"""

