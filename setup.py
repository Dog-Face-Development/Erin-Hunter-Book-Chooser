import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

setup( name = 'Erin Hunter Book Chooser' ,
            version = '3.0' ,
           description = 'Choose\'s Erin Hunter books.' ,
           author = 'William Vandergraaf' ,
           option = { 'build_exe' : opts } ,
           executable = [ Executable( "Erin Hunter Book Chooser Main Window.py" , base = base ) ] )
                      
