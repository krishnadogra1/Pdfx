from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["txtfile"]
        if file and file.filename.endswith(".txt"):
            filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            txt_path = os.path.join(UPLOAD_FOLDER, "temp.txt")
            pdf_path = os.path.join(UPLOAD_FOLDER, filename)

            file.save(txt_path)
            convert_to_pdf(txt_path, pdf_path)

            return send_file(pdf_path, as_attachment=True)

    return render_template("index.html")

def convert_to_pdf(txt_file, pdf_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    with open(txt_file, "r", encoding="utf-8") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf.output(pdf_file)

if __name__ == "__main__":
    app.run(debug=True)
