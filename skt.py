from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m   =============================================')
           print('')
           os.system('figlet "           Login" | lolcat')
           print("\033[1;93m")
           print('   =============================================')
           print('')
           print("\033[1;35m             Login Dulu Bngst")
           print("")
           try:
                l = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                p = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if l=="Mr.p3mu14" and p=="Hack" or l=="Lmc" and p=="Muslim" or l=="free" and p=="":
                   time.sleep(1)
                   print('\033[1;33m   Login Berhasil Tod...\033[0m')
                   time.sleep(1)
                   os.system('clear')
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Username Salah Tod..")
                      time.sleep(2)
                      print("")
           except Exception:
                      os.system("rm -rf lock.py")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Username Yang Anda Masukan Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      os.system("rm -rf lock.py")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("Thanks You :*")
                      time.sleep(2)
                      os.system("clear")
                      exit()
menu()
