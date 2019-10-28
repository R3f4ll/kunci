import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  jangan memperjual belikan tools ini')
print(b+'\t    Mr.R3f4ll')
print('\t GITHUB=https://github.com/R3f4ll')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] tools sedang berjalan..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+a+'\n\nhubungi Mr.R3f4ll JIKA ADA MASALAH\nThanks TO :Mr.R3f4ll\n[!] Restart Termux Anda\n\n')

# semoga bermanfaat
# BY=Mr.R3f4ll

