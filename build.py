from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    "packages": ["os", "sys", "PyQt5", "qfluentwidgets"],
    "include_files": ["ui/resources/icon.png"]
}

setup(
    name = "FREE PANEL",
    version = "0.1",
    description = "My PyQt5 application",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, icon="ui/resources/icon.png")]
)
