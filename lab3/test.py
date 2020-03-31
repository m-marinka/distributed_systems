import asyncio
import codecs
import sys
import socket
import time
import signal
from timeit import default_timer as timer

host = "localhost"  # input("Enter the ip: ")
port = 4321  # int(input("enter the port: "))
maxCount = 2
count = 0
passed = 0
failed = 0


# name = input("Input the command: ")

def getResults():
    lRate = 0
    if failed != 0:
        lRate = failed / (count) * 100
        lRate = "%.2f" % lRate

    print("\nTCP Ping Results: Connections (Total/Pass/Fail): [{:}/{:}/{:}] (Failed: {:}%)".format((count), passed,
                                                                                                   failed, str(lRate)))


def signal_handler(signal, frame):
    """ Catch Ctrl-C and Exit """
    getResults()
    sys.exit(0)


# Register SIGINT Handler
signal.signal(signal.SIGINT, signal_handler)

# Loop while less than max count or until Ctrl-C caught
while count < maxCount:

    # Increment Counter
    count += 1

    success = False

    # New Socket
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    # 1sec Timeout
    s.settimeout(1)

    # Start a timer
    s_start = timer()

    # Try to Connect
    try:
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)
        success = True
    except socket.timeout:
        print("Connection timed out!")
        failed += 1
    except OSError as e:
        print("OS Error:", e)
        failed += 1

    # Stop Timer
    s_stop = timer()
    s_runtime = "%.2f" % (1000 * (s_stop - s_start))

    if success:
        print("Connected to %s[%s]: tcp_seq=%s time=%s ms" % (host, port, (count - 1), s_runtime))
        passed += 1

    # Sleep for 1sec
    if count < maxCount:
        time.sleep(1)

    # Output Results if maxCount reached


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection(host, port,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode('utf-8'))

    data = await reader.read(100)
    print('Received: %r' % data.decode('utf-8'))
    print('Close the socket')
    writer.close()


message = input("enter the message: \n ")
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))

ext = input("type exit to escape: ")


if ext == "exit":
    loop.close()

getResults()
