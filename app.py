from flask import Flask, render_template, request, jsonify, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import io

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/generate-pdf", methods=["POST"])
def generate_pdf():
    payload = request.get_json(force=True)
    title = (payload or {}).get("title", "Generated Report").strip() or "Generated Report"
    author = (payload or {}).get("author", "Gaurav Jain").strip() or "Gaurav Jain"
    content = (payload or {}).get("content", "").strip() or "No content provided."

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle(title)
    pdf.setAuthor(author)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(72, 750, title)
    pdf.setFont("Helvetica", 11)
    pdf.drawString(72, 730, f"Prepared by: {author}")

    y = 700
    for line in content.splitlines():
        if not line.strip():
            y -= 18
            continue
        for wrapped_line in simpleSplit(line, "Helvetica", 11, letter[0] - 144):
            if y < 72:
                pdf.showPage()
                pdf.setFont("Helvetica", 11)
                y = 750
            pdf.drawString(72, y, wrapped_line)
            y -= 18

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="generated-report.pdf",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
