# Secure System with digital envelope
secure system having confidentiality,integrity and authentication using digital envelope

In this I have implemented a system having confidentiality, integrity and authentication
we have calculated our own hash value 
symmetric key is not known earlier to sender and receiver they will be shared

1. firstly client is connected to server
2. next client will input key x
3. hash value of key will be genereated entered by the client
4. hash value will be encrypted by sender here client private key to provide authentication
5. key x will be encrypted using receiver public key 
6. both encrypted key and encrypted hash send to server
7. server will decrypt key using public key of client
8. decrypt msg using his private key
9. check hash if same then verified user
10. also repeat same step and generate key so client also authenticate
11. both side authentication complete
12. for simplicity here take symmetric key as x*y i.e client key*server key
13. now both will communicate using their symmetric key

server:

![image](https://user-images.githubusercontent.com/89848299/201416393-bcc11e0f-afb4-4cc0-b642-0aaf69fbb37d.png)


client:

![image](https://user-images.githubusercontent.com/89848299/201416474-09ab6ab1-851b-46d2-ac20-52033203dc80.png)
