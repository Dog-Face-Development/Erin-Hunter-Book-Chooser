import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = { 'include_files' : ['ArchitectsDaughter.ttf'] , 'includes' : ['re'] }

setup( name = 'Erin Hunter Book Chooser' ,
       version = '5.0' ,
       description = "Select's Erin Hunter books based on your favorite animal. Now includes a new Erin Hunter series!" ,
       author = 'William Vandergraaf' ,
       option = { 'build_exe' : opts } ,
       executable = [ Executable( "Erin Hunter Book Chooser Main Window.py" , base = base ) ] )
                      
