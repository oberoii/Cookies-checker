from flask import Flask, render_template, request

app = Flask(__name__)

def validate_cookie_format(cookie_text):
    """
    Simple format validation:
    - key=value pairs
    - separated by semicolons
    """
    if not cookie_text:
        return False

    pairs = cookie_text.split(";")
    for pair in pairs:
        if "=" not in pair:
            return False
        key, value = pair.split("=", 1)
        if not key.strip() or not value.strip():
            return False

    return True


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        cookies = request.form.get("cookies")
        if validate_cookie_format(cookies):
            result = "VALID COOKIE FORMAT ✅"
        else:
            result = "INVALID COOKIE FORMAT ❌"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
