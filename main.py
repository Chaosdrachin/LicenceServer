import socket
import os
import random
import threading
from sklearn.linear_model import LinearRegression
import math

preGen = ""

# Set Security-Salt
salt = ["K$", "To", "P/", "&$GU", "ZzF", "%He", "%%hheUR", "Dra%g0N", "S4l1y", "M0Ar$", "%Sa17",
        "Uu", "!&", "/DkL", "[O]",  "Lp", "ErR", "%HK$", "DeT§", "%Rr&aW", "SzZ$B" "&UOg$", "$§"]

Serverconfigs = []
Serverconfig = open("LicenceConfig.chaos", "r")
# Preprocess - Config Files
for line in Serverconfig:
    line = line.replace("\n", "")
    line = line.replace("ComHostIp=", "")
    line = line.replace("ComHostPort=", "")
    Serverconfigs.append(line.lower())

# Salt Function
def Salty_Dragon(result):
    # Make The predicted hash Salty
    end_result = str(result).replace("-", "")
    len_of_result = len(end_result)
    distance_of_salt = len(salt)
    len_of_result = int(math.ceil(len_of_result / distance_of_salt))
    test = []
    count = 0
    i = 0
    for N in end_result:
        test.append(N)
        count += 1
        if count == len_of_result:
            i += 1
            test.append(salt[i])
            count = 0
    # Return SaltedHash
   # print("The Predicted Hash Salted : " + str(test.txt).replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("'","").replace("-", ""))
    return str(test).replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("'","").replace("-", "")

# CreateKey
def Create_licencekey():
    X = [
        [107101118105110], [115118101110], [9711010011410197115], [102979810597110],
        [97108101120], [1159798105110101], [1089711711497], [116101117102101108]]

    Y = [659889646, 400115018, 252931470, 757031276, 420869874, 842788406, 352931470, 9129204603]

    model = LinearRegression()
    model.fit(X, Y)
    randomNumb = random.randint(107101118105110, 9711010011410197115)
    result = model.predict([[randomNumb], [0]])
    result = math.floor(result[0])
    result = Salty_Dragon(result)
    return str(result)

def TimeBasdCreation():
    newKey = "NewOne"

    preGen = newKey

def serverStart():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (Serverconfigs[0], int(Serverconfigs[1]))
    sock.bind(server_address)
    print('starting up on {} port {}'.format(*sock.getsockname()))
    sock.listen(1)
    # ------------------------------------------ Kern Schleife -------------------------------------------------- #
    while True:
        print('waiting for a connection\n')
        connection, client_address = sock.accept()
        try:
            while True:
                data = connection.recv(2048)
                data = data.decode('utf-8')
                if data == "7964A39FD138E6D456F8CCF43D2556E108055BF38303788E35F4BFD05D3E80A9":
                    print("[*][KEY_Request] from ", client_address)
                    # Check Saved Data
                    print("[*][SET] KEY for Send")
                    key = preGen
                    # Send Answer
                    print("[*][SEND] key...")
                    connection.sendall(key.encode('utf-8'))
                    print("[+] Key Sent")
                    break
            print("[*] Close Connection")
            connection.close()
            print("[+] Done")
        except Exception as err:
            os.system("echo " + str(err) + " > ErrorLog.txt")
            print(err)

# Banner
os.system("clear")
print("""
####################################
#         Licence-Server           #
#         Module V-0.1.0           #
#            by Wyv3rn             #
####################################
""")
# Generate Key on Start
print("[*] Pregenerate First Key")
preGen = Create_licencekey()
print("[+] Key Generated : " + preGen)
# StartMainServer Thread
threading.Thread(target=serverStart).start()
# TimeBasedKeyCreation
threading.Thread(target=TimeBasdCreation).start()
