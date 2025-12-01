
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json