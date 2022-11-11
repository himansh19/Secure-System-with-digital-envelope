import socket
import math
import random
import pickle

# skey=4
# Create a socket object
s = socket.socket()
print("Socket successfully created")
# Define the port on which you want to connect
port = 1234

# connect to the server on local computer
s.bind(('', port))

# put the socket into listening mode
s.listen(1)
print("Waiting for Connections")

puc=(997,323)
prs=(733,899)
pus=(997,899)



# -----------------------------------------------------------------------------------------------------------------------


def sencrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if(char.isspace()):
            # spc=400
            result+='*'
        # Encrypt uppercase characters
        elif (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def sdecrypt(text, s):
    s = 26 - s
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if(char=='*'):
            # spc=400
            result+=' '
        # Encrypt uppercase characters
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def hash1(stri):
    inc=2
    for i in stri:
        m=ord(i)*inc
        inc+=1
    
    return m%1000
    

def encrypt(pub_key,n_text):
    e,n=pub_key
    x=""
    m=0
    for i in n_text:
        if(i.isspace()):
            # spc=400
            x+='*'
        else:               
            m= ord(i)
            c=(m**e)%n
            x+=chr(int(c))
    return x

def decrypt(priv_key,c_text):
    d,n=priv_key
    x=''
    m=0
    for i in c_text:
        if(i=='*'):
            x+=' '
        else:
            m=(ord(i)**d)%n
            c=chr(m)
            x+=c
    return x

def enchash(k1,h1):
    e,n=k1
    x=''
    while(h1>0):
        temp1=int(h1%10)
        c=(temp1**e)%n
        h1=h1/10
        x+=chr(c)
    return x
def dechash(k2,h2):
    d,n=k2
    x=0
    # h2=h2[-1::-1]     # reverse
    # print(h2)
    y=1
    for i in h2:
        temp1=(ord(i)**d)%n
        # print(temp1)
        x+=y*temp1
        y=y*10
        # print(x)
    return x

def d1(tex):
    x=''
    for i in tex:
        if(i=='@'):
            x1=x  
            x=''  
        else:
            x+=i
    print(x1,x)
    return x1,x

c, addr = s.accept()  # accept() returns a tuple
# print('Got connected with', addr)
n1 = c.recv(1024)
print('Got connected with', addr, n1.decode())

recreq = c.recv(1024).decode()    # receive hias reuest
print('received encrypted text: ',recreq)
recdat,recenhas=d1(recreq)  # decrypt to get data & hash
recdecdat=decrypt(prs,recdat)
print('decrypted msg using symmetric key : ',recdecdat)
print('decrypted hash: ',recenhas)

rechas1=hash1(recdecdat)    #calculate hash value of received data
print('Hash of msg received: ',rechas1)
rechas=dechash(puc,recenhas)   #decr hash using puc
print('Actual hash received: ',rechas)


if(rechas1==rechas):
    print('Client is authorized')
    name = input("Enter key: ")
    hreq=hash1(name)    #calculate hash
    print('Hash value of request: ',hreq)
    ehas=enchash(prs,hreq)   #encrypt hash
    print('Encrypted hash value using private key: ',ehas)
    
    signdata=encrypt(puc,name)   # encrypt data using public key of server
    print('encrypted data using symmetric key: ',signdata)
    combsigdat=signdata+'@'+ehas
    
    print('value to send: ',combsigdat)

    c.send(combsigdat.encode())

    skey=int(name)*int(recdecdat)
    print('symmetric key: ',skey)
    while True:
        # Establish connection with client.
        # ---------------------------------------------------------------------------------------------------------------------
        # Message recieved from the client and prints in the terminal
        msg = c.recv(1024).decode()

        print("-> Encrypted message:", msg)
        
        print(f'-> Received Message: ', sdecrypt(msg,skey))
        str = input("------> ")
        str1=sencrypt(str,skey)
        
        c.send(str1.encode())

else:
    print('Unauthorized client send')




