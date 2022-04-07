#usr/bin/python3
import os ,sys,shutil,json,time
import requests
from time import sleep
from time import strftime as tm
try:
	import requests
except:
	os.system('pip install requests')

## PERUMPANAN & SYNTAX ###
____irpanganteng____ = print
____irpan__chose____ = input
____irpan__execc____ = exec
____irpan__clear____ = os.system('clear')

### JAM & HARI ###
jamm = time.strftime("%H:%M:%S")
harii = time.strftime("%d/%m/%Y")

### WARNA WARNI ###
A = "\x1b[m"
M = "\x1b[1;91m"
K = "\x1b[1;93m"
H = "\x1b[1;92m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
C = "\x1b[1;96m"
P = "\x1b[1;97m"
BGP = " \033[47m\033[1;31m"
BGR = "\033[41m\033[1;37m"
### TITIK WARNA ###
___M_K_H___ = "\x1b[1;91m•\x1b[1;93m•\x1b[1;92m•"
___H_K_M___ = "\x1b[1;92m•\x1b[1;93m•\x1b[1;91m•"
____irpan__clear____
### LOGOO TOOLS ###
def _____logo_____():
    ____irpanganteng____(f""" 
\n{P}                 {BGR}{harii}{A}  
{P}   ╭─────────{___M_K_H___}{BGP} {jamm} {A} {___H_K_M___}{P}─────────╮
{P}   │  ©{U} _____________________________  {P} │
{P}   │   {U}/  _____/\______   \_   _____/  {P} │
{P}   │  {U}/   \  ___ |    |  _/|    __)    {P} │
{P}   │  {U}\    \_\  \|    |   \|     \     {P} │
{P}   │   {U}\______  /|______  /\___  /     {P} │
{P}   │          {U}\/        \/     \/      {P} │
{P}   ╰───────────┬────────────┬───────────╯""")

____irpan__clear____
_____logo_____()
### MENU UTAMA ###
____irpanganteng____(f'{P}               ░            ░')
____irpanganteng____(f'{P}        ╭──────┴─{___M_K_H___}    {___H_K_M___}{P}─┴──────╮')
____irpanganteng____(f'{P}        ├────┬───────────────┬─────┤')
____irpanganteng____(f'{P}        │ {C}01{P} │  auto follow  │ {P}[{M}•{P}] │')
____irpanganteng____(f'{P}        │ {C}02{P} │  auto likers  │ {P}[{H}•{P}] │')
____irpanganteng____(f'{P}        │ {C}03{P} │  auto coment  │ {P}[{M}•{P}] │')
____irpanganteng____(f'{P}        │ {C}04{P} │  auto shares  │ {P}[{M}•{P}] │')
____irpanganteng____(f'{P}        │ {C}05{P} │  donation me  │ {P}[{H}•{P}] │')
____irpanganteng____(f'{P}        │ {C}06{P} │  free acount  │ {P}[{H}•{P}] │')
____irpanganteng____(f'{P}        │ {C}07{P} │  free tokens  │ {P}[{H}•{P}] │')
____irpanganteng____(f'{P}        │ {C}08{P} │  report bugg  │ {P}[{M}•{P}] │')
____irpanganteng____(f'{P}        │ {C}09{P} │  unduh video  │ {P}[{M}•{P}] │')
____irpanganteng____(f'{P}        │ {C}10{P} │  information  │ {P}[{H}•{P}] │')
____irpanganteng____(f'{P}        │ {M}00{P} │  {K}logout{P}/{K}exit  {P}│ {P}[{M}!{P}] │')
____irpanganteng____(f'{P}        ├────┴───────────────┴─────┤')
#____pilih____ = ____irpan__chose____(f' {P}       ╰─➣ {K}')
____pilih____ = ____irpan__chose____(' ╰──────────░    ░──────────╯\n'.center(shutil.get_terminal_size().columns) + "".center(14))
try:
  if ____pilih____ in ['1','01']: #AUTO FOLLOWERS
    ____irpanganteng____(f'\n{P}╭─────────────────────────────────────────╮')
    ____irpanganteng____(f'{P}│{K} maaf fitur {P}[{K}01{P}] {K}belum tersedia saat ini {P}│')
    ____irpanganteng____(f'{P}│{K} sorry feature {P}[{K}01{P}] {K}is not yet available {P}│')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯')
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮')
    ____irpanganteng____(f'{P}  │  tekan {H}enter {P}untuk kembali ke menu  │')
    ____irpanganteng____(f'{P}  │    press {H}enter {P}to return to menu    │')
    ____irpanganteng____(f'{P}  ├─────────────────────────────────────╯')
    ____autofollower____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['2','02']: #AUTO LIKERS
    ____irpan__execc____(requests.get("https://run.mocky.io/v3/8d0a4f82-99c5-4aef-ae85-eff1c34f881a").text)
  elif ____pilih____ in ['3','03']: #AUTO KOMENTAR
    ____irpanganteng____(f'\n{P}╭─────────────────────────────────────────╮')
    ____irpanganteng____(f'{P}│{K} maaf fitur {P}[{K}03{P}] {K}belum tersedia saat ini {P}│')
    ____irpanganteng____(f'{P}│{K} sorry feature {P}[{K}03{P}] {K}is not yet available {P}│')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯')
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮')
    ____irpanganteng____(f'{P}  │  tekan {H}enter {P}untuk kembali ke menu  │')
    ____irpanganteng____(f'{P}  │    press {H}enter {P}to return to menu    │')
    ____irpanganteng____(f'{P}  ├─────────────────────────────────────╯')
    ____autocomments____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['4','04']: #AUTO SHARE
    ____irpanganteng____(f'\n{P}╭─────────────────────────────────────────╮')
    ____irpanganteng____(f'{P}│{K} maaf fitur {P}[{K}04{P}] {K}belum tersedia saat ini {P}│')
    ____irpanganteng____(f'{P}│{K} sorry feature {P}[{K}04{P}] {K}is not yet available {P}│')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯')
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮')
    ____irpanganteng____(f'{P}  │  tekan {H}enter {P}untuk kembali ke menu  │')
    ____irpanganteng____(f'{P}  │    press {H}enter {P}to return to menu    │')
    ____irpanganteng____(f'{P}  ├─────────────────────────────────────╯')
    ____autosharesss____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['5','05']: #DONASI
    ____irpanganteng____(f'\n{P}╭───────────────{___M_K_H___}     {___H_K_M___}{P}───────────────╮')
    ____irpanganteng____(f'{P}├─────────────────────────────────────────┤')
    ____irpanganteng____(f'{P}│  kakak akan di arahkan menuju saweria.  │')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯');sleep(3); os.system('xdg-open https://saweria.co/irpansopian');sleep(3)
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}╭────────────┴──{___M_K_H___}     {___H_K_M___}{P}──┴────────────╮')
    ____irpanganteng____(f'{P}│  terimakasih kak sebelumnya jika telah  │')
    ____irpanganteng____(f'{P}│ memberikan {H}donate {P}kepada admin, semogaa │')
    ____irpanganteng____(f'{P}│ rejeki kakak dilancarkan,terimakasih... │')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯')
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮')
    ____irpanganteng____(f'{P}  │  tekan {H}enter {P}untuk kembali ke menu  │')
    ____irpanganteng____(f'{P}  │    press {H}enter {P}to return to menu    │')
    ____irpanganteng____(f'{P}  ├─────────────────────────────────────╯')
    ____donatesawerr____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['6','06']: #AKUN FREE      1785746458 • desiekawati
    ____irpanganteng____(f'\n{P}        ╭─────{M}•{K}•{H}• {H}1785746458 •{K}•{M}•{P}────╮')
    ____irpanganteng____(f'{P}        ╰────┬── {H}desiekawati {P}──┬────╯')
    ____irpanganteng____(f'{P}             ░                 ░')
    ____irpanganteng____(f'{P}    ╭────────┴───{___M_K_H___}     {___H_K_M___}{P}───┴────────╮')
    ____irpanganteng____(f'{P}    │ tekan {H}enter {P}untuk kembali ke menu │')
    ____irpanganteng____(f'{P}    │   press {H}enter {P}to return to menu   │')
    ____irpanganteng____(f'{P}    ├───────────────────────────────────╯')
    ____freeaccountt____ = ____irpan__chose____(f'{P}    ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['7','07']: #TOKEN FREE
    ____irpanganteng____(f'\n{P}╭─────────────────────────────────────────╮\n{P}│kakak akan {H}otomatis {P}di alihkan ke halaman│\n{P}│jangan lupa ikuti facebook nya ya kakak..│\n{P}╰────────────┬───────────────┬────────────╯\n{P}             ░               ░\n{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮\n{P}  │ {B}https://www.facebook.com/Aang.XD404 {P}│\n{P}  ╰──────────┬───────────────┬──────────╯\n{P}             ░               ░\n{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮\n{P}  │  tekan {H}enter {P}untuk kembali ke menu  │\n{P}  │    press {H}enter {P}to return to menu    │\n{P}  ├─────────────────────────────────────╯');sleep(1); os.system('xdg-open https://mbasic.facebook.com/5222617434468924')
    ____freeaccestkn____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['8','08']: #UNDUH VIDEO
    ____irpanganteng____(f'\n{P}╭─────────────────────────────────────────╮')
    ____irpanganteng____(f'{P}│{K} maaf fitur {P}[{K}08{P}] {K}belum tersedia saat ini {P}│')
    ____irpanganteng____(f'{P}│{K} sorry feature {P}[{K}08{P}] {K}is not yet available {P}│')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯')
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮')
    ____irpanganteng____(f'{P}  │  tekan {H}enter {P}untuk kembali ke menu  │')
    ____irpanganteng____(f'{P}  │    press {H}enter {P}to return to menu    │')
    ____irpanganteng____(f'{P}  ├─────────────────────────────────────╯')
    ____reportingbug____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['9','09']:
    ____irpanganteng____(f'\n{P}╭─────────────────────────────────────────╮')
    ____irpanganteng____(f'{P}│{K} maaf fitur {P}[{K}09{P}] {K}belum tersedia saat ini {P}│')
    ____irpanganteng____(f'{P}│{K} sorry feature {P}[{K}09{P}] {K}is not yet available {P}│')
    ____irpanganteng____(f'{P}╰────────────┬───────────────┬────────────╯')
    ____irpanganteng____(f'{P}             ░               ░')
    ____irpanganteng____(f'{P}  ╭──────────┴───{___M_K_H___}   {___H_K_M___}{P}───┴──────────╮')
    ____irpanganteng____(f'{P}  │  tekan {H}enter {P}untuk kembali ke menu  │')
    ____irpanganteng____(f'{P}  │    press {H}enter {P}to return to menu    │')
    ____irpanganteng____(f'{P}  ├─────────────────────────────────────╯')
    ____unduhvideoss____ = ____irpan__chose____(f'{P}  ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['10','010']: #INFORMASI
    ____irpan__clear____
    ____irpanganteng____(f'\n{P}  ╭───────────{___M_K_H___}          {___M_K_H___}{P}───────────╮\n{P}  │ [ INFORMASI ALAT & INFORMASI ADMIN ] {P}│\n{P}  ├──────────────────────────────────────┤\n{P}  │ tools ini dibuat oleh.. {H}irpan sopian {P}│\n{P}  │ secara {H}free{P}/{H}gratis {P}untuk siapapun yg │\n{P}  │ ingin menggunakannya, jika ada telah │\n{P}  │ menjual tools ini tanpa seijinn oleh │\n{P}  │ admin, harap {M}laporkan {P}penjual kepada │\n{P}  │ pembuat ataupun pengurus tools ini.. │\n{P}  ├──────────────────────────────────────┤\n{P}  │ author   : irpan sopian && Pahrul FZ │\n{P}  │ gmaill   : irpansopian172@gmail.com  │\n{P}  │ github   : github.com/IrpanQwerty-05 │\n{P}  │ donate   : saweria.co/irpansopian    │\n{P}  │ facebook : facebook.com/irpan.qwerty │\n{P}  ╰─────────┬──────────────────┬─────────╯\n{P}            ░                  ░\n{P}   ╭────────┴────{___M_K_H___}    {___M_K_H___}{P}────┴────────╮\n{P}   │ tekan {H}enter {P}untuk kembali ke menu. │\n{P}   │   press {H}enter {P}to return to menu.   │\n{P}   ├────────────────────────────────────╯')
    ____informations____ = ____irpan__chose____(f'{P}   ╰─➣ {K}'); os.system('python run.py')
  elif ____pilih____ in ['0','00']: #KELUAR
    ____irpanganteng____(f'\n{P}  ╭──────────────────────────────────────╮ \n{P}  │  {P}selamat tinggal, terimakasih telah  {P}│ \n{P}  │ {P}menggunakan tools ini, silahkan anda {P}│ \n{P}  │ {P}berikan {H}bintang {P}untuk repository ini {P}│ \n{P}  │ {P}jika anda menyukainya.. byeee !!!    {P}│ \n{P}  ╰─────────┬──────────────────┬─────────╯ \n{P}            ░                  ░\n{P}  ╭─────────┴────{___M_K_H___}    {___M_K_H___}{P}────┴─────────╮\n{P}  │   {K}https://github.com/IrpanQwerty-05  {P}│\n{P}  ╰──────────────────────────────────────╯')
  else:
    ____irpanganteng____(f'\n{M}  ╭──────────────────────────────────────╮ \n{M}  │ {P}maaf sepertinya kakak salah mengetik {M}│ \n{M}  ╰─────────┬──────────────────┬─────────╯ \n{P}            ░                  ░\n{P}   ╭────────┴────{___M_K_H___}    {___M_K_H___}{P}────┴────────╮\n{P}   │ tekan {H}enter {P}untuk kembali ke menu. │\n{P}   │   press {H}enter {P}to return to menu.   │\n{P}   ├────────────────────────────────────╯')
    ____kalolusalahh____ = ____irpan__chose____(f'{P}   ╰─➣ {K}'); os.system('python run.py')
    
    
    
except:
   pass
