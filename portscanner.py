import socket
import sys
import time
import argparse

def scan(targets,port):
    try:
        soc=socket.socket()
        socket.setdefaulttimeout(1)
        result=soc.connect_ex((targets,port))
        if result==0:
            print("Port {} is open.".format(port))
        soc.close()
    
    except KeyboardInterrupt:
        print("\nExiting Program....")
        sys.exit()
    except socket.gaierror:
        print("[Error] Failure in name resolution.(No known DNS)")
        sys.exit()
    except socket.error:
        print("Waiting for server to respond...")
        time.sleep(2)
        print("[Error]Serveer not responding. Exiting Program....")
        sys.exit()

parser=argparse.ArgumentParser(description='Scans the open port in the target device.')
parser.add_argument("ip",help="IP Adress of the target device.")
parser.add_argument("-p","--port", help="Specific ports you want to scan.(Not usable with -r )", nargs='+')
parser.add_argument("-r","--range",help="Range of the ports you want to scan.Starts with 1.(Not usable with -p.)", nargs=1)
args=parser.parse_args()

target=args.ip
if args.port!=None and args.range!=None:
    print("[Error] Invalid Argument")
    sys.exit()

if args.port!=None:
    for ports in arg,port:
        scan(target,int(ports))

if args.range!=None:
    ran=args.range

if args.port==None and args.range==None:
    for x in range(1,65535):
        scan(target,x)