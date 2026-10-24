from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import os
import json,re,math,zipfile,io,zlib,base64
from pathlib import Path
R=Path(__file__).parent
SK='python java javascript react node.js html css sql mysql postgresql flask django machine learning nlp pandas numpy tensorflow pytorch excel aws azure docker git linux api leadership teamwork'.split()
def extract(b,e):
 if e=='.docx':
  with zipfile.ZipFile(io.BytesIO(b)) as z:s=z.read('word/document.xml').decode('utf8','ignore')
  return re.sub(r'<[^>]+>',' ',s)
 o=[]
 for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream',b,re.S):
  x=m.group(1);d=b[max(0,b.rfind(b'<<',0,m.start())):m.start()]
  try:
   if b'FlateDecode' in d:x=zlib.decompress(x)
   o += [q.decode('latin1','ignore') for q in re.findall(rb'\(([^()]*)\)\s*Tj',x)]
  except:pass
 return ' '.join(o)
def analyze(n,t,j):
 skills=lambda s:[k for k in SK if re.search(r'(?<![a-z0-9])'+re.escape(k)+r'(?![a-z0-9])',s.lower())]
 a=skills(t);b=skills(j);hit=[x for x in b if x in a];miss=[x for x in b if x not in a];lo=t.lower();sec=sum(any(w in lo for w in g) for g in [('experience','employment'),('education','degree'),('skills','technologies'),('project',),('summary','profile')]);s=min(100,35+sec*13);ats=min(100,48+12*bool(re.search(r'@',t))+3*len(a));impact=min(100,42+10*len(re.findall(r'\d+%|\b(?:built|led|improved|created|delivered)\b',lo)));sim=round(100*len(hit)/max(1,len(b))) if j.strip() else 0;ready=round(min(100,38+4*len(a))*.38+s*.22+impact*.2+(len(hit)/max(1,len(b))*100 if b else 72)*.2);score=round(ats*.25+s*.2+impact*.2+8.2+(sim*.25 if j.strip() else 18));f=[]
 if miss:f.append({'level':'Priority','title':'Show evidence for role skills','body':'Role mentions '+', '.join(miss)+'. Add a real example if you have used them.'})
 if sec<4:f.append({'level':'Improve','title':'Make key sections easy to scan','body':'Use clear headings for experience, education, skills, and projects.'})
 if not j.strip():f.append({'level':'Note','title':'Add a job description','body':'Role match is excluded until you add a target job description.'})
 if not f:f=[{'level':'Good','title':'A solid starting point','body':'Review matched skills and tailor your strongest evidence to the role.'}]
 qs=['Tell me about a project using '+x+'. What was your contribution and outcome?' for x in (miss+hit+a)[:3]] or ['Walk me through a project you are proud of.']
 return {'name':n,'overall':score,'readiness':ready,'match':sim,'categories':[{'name':'ATS readability','score':ats},{'name':'Resume sections','score':s},{'name':'Impact & clarity','score':impact},{'name':'Job match','score':sim if j.strip() else None},{'name':'Interview readiness','score':ready}],'summary':f'Found {len(a)} skills and {sec} clear sections. Heuristic signals, not a hiring decision.','skills':a,'matched':hit,'missing':miss,'findings':f,'questions':qs,'method':'Local text rules and keyword overlap. No AI service is connected.'}
class H(BaseHTTPRequestHandler):
 def out(self,c,x):
  b=json.dumps(x).encode();self.send_response(c);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(b)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(b)
 def do_GET(self):
  b=(R/'index.html').read_bytes();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(b)
 def do_POST(self):
  try:
   length=int(self.headers.get('Content-Length','0'))
   if length>7100000:return self.out(413,{'error':'Upload is too large; limit is 5 MB.'})
   x=json.loads(self.rfile.read(length));n=Path(x['name']).name;e=Path(n).suffix.lower();b=base64.b64decode(x['data'])
   if len(b)>5*1024*1024:return self.out(400,{'error':'File exceeds 5 MB.'})
   if e not in ('.pdf','.docx'):return self.out(400,{'error':'Choose a PDF or DOCX.'})
   t=extract(b,e)
   if len(t)<20:return self.out(422,{'error':'Could not read text. Scanned PDFs need OCR.'})
   self.out(200,analyze(n,t,x.get('jd','')))
  except:self.out(400,{'error':'Could not read the file. Try another PDF or DOCX.'})
 def log_message(self,*a):pass
if __name__=='__main__':
 port=int(os.environ.get('PORT','8000'));print(f'Resume analyzer listening on port {port}');ThreadingHTTPServer(('0.0.0.0',port),H).serve_forever()
