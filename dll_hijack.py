import pymem
import subprocess
import os
import time


notepad = subprocess.Popen(['notepad.exe'])


mem = pymem.Pymem("notepad.exe")


mem.inject_python_interpreter()




code = """
import subprocess
import time
calc=subprocess.Popen(['calc.exe'])

"""

mem.inject_python_shellcode(code)


notepad.kill()
