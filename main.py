import os

def move(folder,files):
    for file in files:
        os.replace(file,f"{folder}/{file}")

dirs=['Images','pdf','Python_files','others','Medias']
pdf_ext=['pdf']
img_ext=['jpg','jpeg','png']
pyth_ext=['py','csv']
media_ext=['mp3','mp4','mkv']


for i in dirs:
    try:
        os.makedirs(i)   
    except Exception:
        pass
# files = os.listdir(os.curdir)

files=[file for file in os.listdir(os.curdir) if not os.path.isdir(file)]
files.remove('main.py')

pdf=[file for file in files if file.split('.')[-1].lower() in pdf_ext] 

img=[file for file in files if file.split('.')[-1].lower() in img_ext] 

pyth=[file for file in files if file.split('.')[-1].lower() in pyth_ext] 

media=[file for file in files if file.split('.')[-1].lower() in media_ext] 


oth=[]
for file in files:
    ext=file.split('.')[-1].lower()
    all_ext=pdf_ext+img_ext+pyth_ext+media_ext
    if ext not in all_ext:
        oth.append(file)

move("images",img)
move("pdf",pdf)
move("Python_files",pyth)
move("others",oth)
move("Medias",media)