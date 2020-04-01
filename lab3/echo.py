import asyncio

host = "localhost"  # input("Enter the ip: ")
port = 4321  # int(input("enter the port: "))
maxCount = 2
count = 0
passed = 0
failed = 0

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