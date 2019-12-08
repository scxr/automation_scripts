
import os, time,errno,random

from pathlib import Path
#Dictionary of folder names
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "OSU":[".osk", ".osz"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "DOCUMENTS": [".pdf",".docx"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
#This will organise your files
def organize(mydir):
    for entry in os.scandir(mydir):
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        truepath = mydir+"/"+str(file_path)
        file_format = file_path.suffix.lower()
        print(file_path)
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            print(directory_path)
            directory_path.mkdir(exist_ok=True)
            try:
                os.rename(truepath,mydir+"/"+str(directory_path)+"/"+str(file_path))
                print("moved "+truepath+" to " + (mydir+"/"+str(directory_path)+"/"+str(file_path)))
            except OSError as e:
                if e.errno == errno.EEXIST:
                    os.rename(truepath,mydir+"/"+str(directory_path)+"/"+str(file_path)+str(random.randint(0,1000)))
                    print("moved "+truepath+" to " + (mydir+"/"+str(directory_path)+"/"+str(file_path)))

            else:
                pass
   #if extension not present in the dctionary than create a folder name "OTHER"
    try:
        os.mkdir("OTHER")
    except Exception:
        pass
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(truepath,mypath + '/OTHER/' + str(Path(dir)))
        except:
            pass
if __name__ == "__main__":
    dir=folder to organise
    organize(dir)
    
