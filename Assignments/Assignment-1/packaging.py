import os
from cx_Freeze import setup, Executable



includefiles = []

build_exe_options = {"packages":["os","numpy","collections","math"]
                     , "excludes":[]
                     ,"include_files":includefiles}

os.environ['TCL_LIBRARY'] = r'C:\Python\Python38\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python\Python38\tcl\tk8.6'

setup(name = "Evolution Algorithms" ,
      version = "0.1" ,
      description = "" ,
      options = {'build_exe': build_exe_options},
      executables = [Executable("hillclimbing.py"), Executable("simulatedAnnealing.py")])