import os
from tkinter.filedialog import askdirectory

caminhoDaPasta = askdirectory(title="Selecione uma pasta para organizar")
lista_arquivos = os.listdir(caminhoDaPasta)

#     locais = {
#          nome da pasta que o arquivo será enviada : extensão do arquivo    
#          }  
  
locais ={
    "imagens": [".png", ".jpg", ".jpeg"],
    "videos" : [".MOV", ".mp4",".mkv", ".avi", ".webm"],
    "audios" : [".mp3", ".wav"],
    "texto"  : [".txt"],
    "pdf"    :  [".pdf"],
    "atalhos": [".lnk"],
    "aplicativos": [".exe", ".msi", ".bat", ".cmd"]
}

for arquivo in lista_arquivos:
    nome, extensao =  os.path.splitext(f"{caminhoDaPasta}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminhoDaPasta}/{pasta}"):
                os.mkdir(f"{caminhoDaPasta}/{pasta}")
            os.rename(f"{caminhoDaPasta}/{arquivo}",f"{caminhoDaPasta}/{pasta}/{arquivo}")

