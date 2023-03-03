import tkinter 
import re, os

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

with open(r"C:\Program Files (x86)\Steam\steamapps\common\Underlords\game\dac\cfg\video.txt", "r") as file:
    string = re.sub(r"setting\.defaultres\"\s{2}\"\d+\"", f"setting.defaultres\"		\"{width}\"", file.read())
    string = re.sub(r"setting\.defaultresheight\"\s{2}\"\d+\"", f"setting.defaultresheight\"		\"{height}\"", string)

with open(r"C:\Program Files (x86)\Steam\steamapps\common\Underlords\game\dac\cfg\video.txt", "w") as file:
    file.write(string)


os.system(r"C:\\\"Program Files (x86)\"\\Steam\\steamapps\\common\\Underlords\\game\\bin\\win64\\underlords.exe")