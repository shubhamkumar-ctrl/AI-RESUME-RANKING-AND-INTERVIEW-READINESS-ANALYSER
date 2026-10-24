# Clearpath — AI Resume Ranking & Interview Readiness Analyzer

Local student prototype: resume text extraction, job keyword matching, simple scoring heuristics, and interview practice prompts. No generative AI or external service is connected.

## Run on Windows
1. Open this folder in File Explorer.
2. Click the address bar, type powershell, and press Enter.
3. Run: py -3.15 app.py (or python app.py if that command works).
4. Keep PowerShell open and visit http://127.0.0.1:8000 in Chrome or Edge.
5. Choose a PDF/DOCX up to 5 MB, optionally paste the job description, then click Check resume.
6. Stop with Ctrl+C.

No pip packages, API key, database, or internet connection is needed. The app listens on 127.0.0.1 only. The browser sends the file to the local server in memory; it is not stored. Scanned PDFs need OCR and are not supported. Scores are heuristic signals, not hiring decisions or ATS guarantees.

If py -3.15 is unavailable, inspect installed versions with py --list and use py -3 app.py or python app.py.
