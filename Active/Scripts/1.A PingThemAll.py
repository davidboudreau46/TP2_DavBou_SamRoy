import subprocess

ActiveIPsList = "Active IPs : \n"

for ping in range(1,256):
    address = "192.168.1." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    print("Pinging : " + address)
    if res == 0:
        ActiveIPsList = ActiveIPsList + address + "\n"

print(ActiveIPsList)

# Inspiré de : http://stackoverflow.com/questions/12101239/multiple-ping-script-in-python
