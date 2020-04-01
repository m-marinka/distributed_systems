import echo
import ping

host = "localhost"  # input("Enter the ip: ")
port = 4321  # int(input("enter the port: "))
maxCount = 2
count = 0
passed = 0
failed = 0

x = input("select command: \n")
if x == "echo":
    echo.tcp_echo_client()
elif x == "ping":
    ping.getResults()

