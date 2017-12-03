import sys
from scapy.all import *
from datetime import datetime
from shutil import copyfile

try:
	interface = raw_input("[*] Enter Desired Interface:")
	ips = raw_input("[*] Enter Range of IPs to scan for: ")
except KeyboardInterrupt:
	print("\n[*] User Requested Shutdown")
	print("[*] Quitting")
	sys.exit(1)
  
print ("\n[*] Scanning....")

start_time = datetime.now()
from scapy.all import srp,Ether,ARP,conf
fileh=open('scan.dat','w+')


conf.verb = 0
ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips),timeout = 2,iface=interface,inter=0.1)


print("Mac -IP\n")
for snd,rcv in ans:
	print(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
        fileh.write(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
	
			
stop_time =datetime.now()
total_time =stop_time - start_time
print("\n[*] Scan Complete!")
print("[*] Scan Duration :%s"%(total_time))
fileh.close()
