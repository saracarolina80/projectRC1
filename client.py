import socket
import signal
import sys
import time
import datetime
from datetime import datetime
import psutil


def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_addr, tcp_port))

while True: 
    try:
        time.sleep(1)
        date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        message = ( "TIME: " + date_time + "CPU: " + str(psutil.cpu_percent()) + "%  Memory: " + str(psutil.virtual_memory()[2]) + "%" ).encode()

        if len(message) > 0:
            sock.send(message)
    
    except (socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)


