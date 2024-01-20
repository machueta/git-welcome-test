import os

class nmappy_scan():
    def recon(ip):
        os.system(f"nmap -A -p- -Pn {ip} -v")
        os.system(f"dirb {ip} ")

    recon(input("What ip would u like to scan? "))

class first(): 
    def ask_info():
        name = str(input("hay, what ur name? "))
        print(f"Helo, {name}!")
        fav_food = str(input(f"{name}, what ur fav food? "))
        print(f"ur fav food is - {fav_food}")
        fav_hob = str(input(f"what ur fav hobby, {name}: "))
        print(f"ur fav hobby is - {fav_hob}")
    

    def ask_age():
        age = int(input(f"what ur aga? "))
        if age <= 5:
            print("u r kid! fucker! go ahead!!")
            return
        if age <= 15:
            print("u r not so kid. whatever, go ahead!!")
            return
        if age <= 21:
            print("not a kid, but ugly. go ahead!")
            return
        if age >= 25:
            print("go ahead, old man!")
            return     
