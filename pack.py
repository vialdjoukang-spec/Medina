import json,glob,os
files=['build_medina.py','test_preview.py','test_medina.py','CHAPTER_SPEC.md','chapters.json','pack.py','engine/medina_course.css','engine/medina_course.js']+sorted(glob.glob('glossary/*.py'))+sorted(glob.glob('chapters/*/*.html'))
json.dump({f:open(f).read() for f in files},open('MEDINA_SOURCES.json','w'),ensure_ascii=False)
print(len(files),os.path.getsize('MEDINA_SOURCES.json'))
# restauration : python3 -c "import json,os;d=json.load(open('MEDINA_SOURCES.json'));[ (os.makedirs(os.path.dirname(k) or '.',exist_ok=True),open(k,'w').write(v)) for k,v in d.items()]"  (+ medora_v6.html requis dans /home/claude)
