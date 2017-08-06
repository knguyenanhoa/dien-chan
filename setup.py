import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
include_files = ["./images/"]
build_exe_options = {"packages": ["os", "kivy"], "excludes": ["tkinter"], "include_files": include_files}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "dien_chan",
        version = "1.0",
        description = "Multireflexology programme",
        options = {"build_exe": build_exe_options}, 
        executables = [Executable("main.py", base = base)])
