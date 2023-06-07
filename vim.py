from pypresence import Presence
from time import time
import sys
import os
try:
    RPC = Presence('1115923695387562034')
    RPC.connect()
    RPC.update(details=f"Editing {sys.argv[1]}",large_image='vim',large_text='vim',start=int(time()))
except:
    pass
os.system(f"vim {sys.argv[1]}")
