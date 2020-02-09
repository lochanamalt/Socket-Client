import socket
import csv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
 
s.bind(('0.0.0.0', 8090 ))
s.listen(0)                 
data = []
with open('xethruData.csv', mode='w' , newline='') as xethruData:
    xethruData_writer = csv.writer(xethruData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    while True:
     
        client, addr = s.accept()
     
        while True:
            content = client.recv(26)
     
            if len(content) ==0:
               break
     
            else:
                dat = content.decode("utf-8")
                line = dat.split(",")
                xethruData_writer.writerow(line)
                print(dat)
