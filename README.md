## Lora-Organizer
A simple program to organize LoRAs for Stable Diffusion

# How To Run 
 
 * For Python run this command (in the directory of the python file)
 `python LoRA_Organization_Program.py`

* You can also just use the .exe (just click it it will ask you the path and it just does evrything be its own)


# Modify??
If you need to modify the code for any reason feel free to do so.

* # What if i also need a .exe file 
Then you need pyinstaller
If you dont have it run this command `pip install pyinstaller`
If for some reason that doesnt work you can also use this 
`Start-Process -NoNewWindow -FilePath "PATH_TO_PYTHON_APPDATA_FOLDER/LocalCache\local-packages\Python310(OR your python version)\Scripts\pyinstaller.exe" -ArgumentList "--onefile", "LoRA_Organization_Program.py"
or if it works for you pyinstaller  LoRA_Organization_Program.py --onefile
(you need pyinstaller for this if you dont have it run pip install pyinstaller)`