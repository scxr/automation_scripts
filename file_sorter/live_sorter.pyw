import os, time,errno,random
from pathlib import Path
#dictionary of folder names from the googles
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

#organise your files function

def organise(mydir):
    for entry in os.scandir(mydir):
        if entry.is_dir():
            continue # we dont want to mess with folders so just leave 
        file_path = Path(entry.name)
        truepath = mydir+"/"+str(file_path)
        file_format = file_path.suffix.lower()
        print(file_path)
        
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            print(directory_path)
            directory_path.mkdir(exist_ok=True)
            
            try:
                os.rename(truepath,mydir+"/"+str(directory_path)+"/"+str(file_path)) # move the file to our dir
                print("moved "+truepath+" to " + (mydir+"/"+str(directory_path)+"/"+str(file_path))) # tell us where its moved
                
            except OSError as e:
                if e.errno == errno.EEXIST:
                    os.rename(truepath,mydir+"/"+str(directory_path)+"/"+str(file_path)+str(random.randint(0,1000))) # if a file with this name already exists
                    print("moved "+truepath+" to " + (mydir+"/"+str(directory_path)+"/"+str(file_path))) # where we moved it to 
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
                os.rename(truepath,mypath + '/OTHER/' + str(Path(dir))) # move our file
        except: 
            pass
        
if __name__ == "__main__":
    while 1:
        dir="directory to organise" # make sure if its a windows dir to make it a raw string
        organise(dir)
        time.sleep(30)
