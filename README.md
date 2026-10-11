# PDF Maker

A Flask app that converts report content into a downloadable, paginated PDF.

## Features
- Rich text input for reports
- Wrapped text and automatic page breaks using ReportLab
- Clean export experience for quick document creation

## Run locally
```bash
cd pdf-maker-portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5001
