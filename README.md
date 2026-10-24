# ClearPath — AI Resume Ranking & Interview Readiness Analyzer

Local student prototype: resume text extraction, job keyword matching, simple scoring heuristics, and interview practice prompts. No generative AI or external service is connected.

## Run locally on Windows
1. Open this folder in File Explorer.
2. Click the address bar, type powershell, and press Enter.
3. Run: py -3.15 app.py (or python app.py if that command works).
4. Keep PowerShell open and visit http://127.0.0.1:8000 in Chrome or Edge.
5. deploy link https://ai-resume-ranking-and-interview-i6tn.onrender.com
6. Choose a PDF/DOCX up to 5 MB, optionally paste the job description, then click Check resume.
7. Stop with Ctrl+C.

## Deploy on Render
This folder contains render.yaml. Put the project files at the root of a GitHub repository, then on Render choose New + > Blueprint and connect that repository. Review the Blueprint and click Apply. Render uses the free Python web service settings from render.yaml. When the deploy is live, open its onrender.com URL. Alternatively create a Web Service manually with Build Command: echo "No third-party packages to install" and Start Command: python app.py. The server reads Render's PORT and binds to 0.0.0.0.

No pip packages, API key, or database is needed. For hosted use, the browser sends the selected resume to the Render server over HTTPS; this app processes it in memory and does not write it to disk. Use sample resumes for a public class demo, not sensitive real resumes. Free services can spin down after inactivity.

Scanned PDFs need OCR and are not supported. Scores are heuristic signals, not hiring decisions or ATS guarantees. Render native Python defaults to its supported runtime; this code does not require Python 3.15 specifically.
