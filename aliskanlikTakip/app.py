from flask import Flask, render_template, request

app = Flask(__name__)

HABITS = [
    "Ders çalıştım",
    "Kitap okudum",
    "Su içtim",
    "Spor yaptım",
    "Erken uyudum"
]

@app.route("/", methods=["GET", "POST"])
def index():
    score = 0
    message = ""
    selected = []

    if request.method == "POST":
        selected = request.form.getlist("habits")
        completed = len(selected)
        not_completed = len(HABITS) - completed

        score = completed * 10 - not_completed * 5

        if score >= 40:
            message = "🎉 Harika bir gün!"
        elif score >= 20:
            message = "🙂 İyi gidiyorsun"
        elif score >= 0:
            message = "😐 Daha iyi olabilir"
        else:
            message = "⚠️ Bugün biraz daha dikkat et"

    return render_template(
        "index.html",
        habits=HABITS,
        score=score,
        message=message,
        selected=selected
    )

if __name__ == "__main__":
    app.run(debug=True)
