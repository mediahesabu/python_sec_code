import socket

#A bare bones TCP client
#Python 2.7
#FRC

target_host = "www.google.com"
target_port = 80

#create my socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((target_host,target_port))

#send data
client.send ("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#get data back
response = client.recv(4096)

print "Server Response begins here:", response