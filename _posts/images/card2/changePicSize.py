import os;

picSize = [274,389]

os.system("pip install Pillow")

#conding=utf8  
import os 
curFileList = os.path.split(os.path.realpath(__file__))
pyFiles = curFileList[0] 

outFilePath = pyFiles + "\\out"
if not os.path.exists(outFilePath):
    os.makedirs(outFilePath) 

g = os.walk(pyFiles)  

picFiles = []

for path,dir_list,file_list in g:  
    for file_name in file_list: 
        file_all_name =  os.path.join(path, file_name)
        file_type  = os.path.splitext(file_all_name)[-1] 
        if file_type == ".png" or file_type == ".jpg":
            picFiles.append(file_all_name)
        

from PIL import Image
 

for file in picFiles: 
    im = Image.open(file)
    out = im.resize((picSize[0],picSize[1]),Image.ANTIALIAS) #resize image with high-quality
    pos = file.rfind('\\')
    outfile = file[0:pos] + '\\out' + file[pos:]
    out.save(outfile)
 