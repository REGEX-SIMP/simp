import os
import platform
print("JOIN FB GROUP")
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    import regex64
    
elif b == '32bit':
    import regex32
