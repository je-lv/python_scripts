#!/usr/bin/python3

"""
Port scanner simple de puertos TCP y UDP en desarrollo como ejercicio.
Escaneos de puertos UDP por arreglar.

"""
import socket
import sys
import subprocess
import re
import datetime

# to colorize output
colors = {
    "OK" : '\33[92m',              #green
    "ERR": '\033[91m',             #red
    "INFO" : '\033[94m',           #blue
    "PROCESS" : '\033[95m',        #purple
    "ENDC" : '\033[0m',            #end of color
    "BOLD" : '\033[1m',            #bold 
}


if len(sys.argv) < 2:                                               
    print(f"{colors['INFO']}Usage: {sys.argv[0]} <IP address> {colors['ENDC']}") 
    sys.exit()
else:
    start = datetime.datetime.now()
    rhost = sys.argv[1]
    #Getting Hostname   
    print(f"[+] Hostname: {socket.gethostbyaddr(sys.argv[1])[0]}")

    #Getting TTL for OS basic detection by pinging rhost
    ping_result, err = subprocess.Popen([f"ping {rhost} -c 1", ""], stdout=subprocess.PIPE, shell=True).communicate()
    #UTF-8 decode bytes respose
    ping_result = ping_result.decode("utf-8")
    #Regex for TTL value
    ttl = int(re.findall(r"(?<=ttl=).\d*", ping_result)[0])
    
    #Basic OS detection with TTL
    if ttl:
        if ttl >= 0 and ttl <= 64:
            print("[+] OS: Linux Machine")
        elif ttl >= 65 and ttl <= 128:
            print("[+] OS: Windows Machine")
        elif ttl >= 129 and ttl <= 254:
            print("[+] OS: Solaris/AIX Machine")
        else:
            print("[!] Unknown OS")
    else:
        print("[!] No TTL detected.")
        pass   


    opentcp_ports = [] 
    openudp_ports = []
    banners = {}                                                
    print(f"{colors['PROCESS']}[+] Port scanning for {rhost}{colors['ENDC']}") 
    
    try:                                                            
        print(f"{colors['OK']}[+] Finding TCP Ports{colors['ENDC']}\n")
        for port in range(1,82):
            #Starting with TCP socket                                  
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  							                                    
            response = s.connect_ex((rhost,port))                    

            if response == 0:                                       
                print(f"{colors['OK']}[+] {port}/TCP Found! {colors['ENDC']}")     
                opentcp_ports.append(port)
                s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = s.recv(1024).decode("utf-8")
                if response == 0:
                    print(f"[+] Banner:\n{banner}")
                else:
                    banner = f"[!] Banner for port {port}/TCP not Found!"
                    print(banner)
                    continue
                
                banners[port] =  banner                 
            s.close()

        print(f"{colors['OK']}[+] Finding UDP Ports{colors['ENDC']}\n")
        for port in range(1,30):
            #UDP Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    				                                     
            response = s.connect_ex((rhost,port))
            try:
                s.send(b"\x00")
            except socket.error as err:
                if err.errno == errno.ECONNREFUSED:
                    banner = f"[!] Banner for port {port}/UDP not Found!"
                    socket.close()
                    break
                else:
                    banner = s.recv(1024).decode("utf-8")
                    print(f"{colors['OK']}[+] {port}/UDP Found! {colors['ENDC']}", end="\tBanner: ")
                    openudp_ports.append(port)
            
                banners[port] =  banner
            s.close()

    #Error Handling section
    except KeyboardInterrupt: 
        print(f"{colors['ERR']}[!] [CTRL] + C was pressed\nExiting Program!{colors['ENDC']}")

    except socket.error as err: 
        print(f"{colors['ERR']}[!] Couldn't connect to the server{colors['ENDC']}")
        sys.exit()


    #open_ports = opentcp_ports + openudp_ports

    with open("results.txt", "w") as results:
        results.write(f"{colors['OK']}Target IP: {rhost}\nOpen Ports:\n{colors['ENDC']}")
        for port,banner in banners.items():
            results.write(f"{port}\n{banner}\n")

print(f"{len(opentcp_ports)} open TCP ports found.")
print(f"{len(openudp_ports)} open UDP ports found.")

print(f"{colors['OK']}[+] Done!{colors['ENDC']}") 
end = datetime.datetime.now()
print(f"Scan duration: {(end - start)*60}")
