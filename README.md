# Lora-Organizer
A simple program to organize LoRAs for Stable Diffusion

## How To Run 
 
 * For Python run this command (in the directory of the python file)
 `python LoRA_Organization_Program.py`

* You can also just use the .exe (just click it it will ask you the path and it just does evrything be its own)


## Modify??
If you need to modify the code for any reason feel free to do so (obvisouly you modify the python file).

## What if I also need a .exe file 
*   Then you need pyinstaller
    If you dont have it run this command `pip install pyinstaller`
    Then run this command `pyinstaller  LoRA_Organization_Program.py --onefile`

*   If for some reason that doesnt work you can also use this 
    (modify to your pc)
    `Start-Process -NoNewWindow -FilePath "PATH_TO_PYTHON_APPDATA_FOLDER/LocalCache\local-packages\Python310(OR your python version)\Scripts\pyinstaller.exe" -ArgumentList "--onefile", "LoRA_Organization_Program.py"`

    Basically you need the path to pyinstaller.exe