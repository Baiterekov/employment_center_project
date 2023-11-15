import docx
import os

Dictionary = {"1": "15"}
paths = []
folder = os.getcwd()
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('docx') and not file.startswith('~'):
            paths.append(os.path.join(root, file))

for path in paths:
    doc = docx.Document(path)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = docx.shared.Pt(48)



    for i in Dictionary:
        for p in doc.paragraphs:
            if p.text.find(i) >= 0:
                p.text = p.text.replace(i, Dictionary[i])

    doc.save("Очередь Шаблон1.docx")
    os.startfile("Очередь Шаблон1.docx", "print")