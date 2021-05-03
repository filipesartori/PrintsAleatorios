from cx_Freeze import setup, Executable
import os
import cx_Freeze
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'

executables=[cx_Freeze.Executable('interface.py')]

cx_Freeze.setup(name='CeasarCypher',version='0.1',description='foda',
      options={'build_exe':{'packages':['tkinter']}},
      executables=executables,
      )