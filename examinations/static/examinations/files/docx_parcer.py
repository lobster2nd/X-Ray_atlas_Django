from docx import Document

doc = Document(
    'C:\Prog\PyCharm\Projects\X-Ray_atlas_Django\examinations\static\examinations\\files'
    '\Kishkovskiy_A_N_Tyutin_L_A_Esinovskaya_G_N_Atlas_ukladok_pri_re.docx')
for paragraph in doc.paragraphs:
    modified_text = paragraph.text.replace('¬', '')
    paragraph.text = modified_text
doc.save(
    'C:\Prog\PyCharm\Projects\X-Ray_atlas_Django\examinations\static\examinations\\files'
    '\Kishkovskiy_A_N_Tyutin_L_A_Esinovskaya_G_N_Atlas_ukladok_pri_re.docx')
