# from the socket module import all
from socket import *
# from the datetime module import all - This is used to get info regarding time and date
from datetime import *
# Create a UDP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Acquires the host name and IP address from the computer using this program
host_name = gethostname()
IP_address = gethostbyname(host_name)

# Prints the Host name and IP address to the console
print('Host name is :: ' + host_name)
print('IP_address :: ' + IP_address)

# set values for host using the host name - meaning this machine and port number 10000
server_address = (host_name, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# we want the server to run all the time, so set up a forever true while loop
client_available = input("Is your client online? Type Y if he/she is :: ")
if client_available == 'Y' or  client_available == 'y':
    # Now the server waits for a connection
    print('*** Waiting for the messages ***')
    # Opens the log file for appending - we don't want old log data to be overwritten
    file = open('client_output.txt', 'a')
    # Writes the time and date that the client jotted the message to the log file
    file.write('Session logged at ' + date.today().strftime("%B %d, %Y") + ' at ' + datetime.now(). strftime("%H:%M:%S") + ' reads\n')

    while True:
        # decode() function returns a tuple object
        # First element is the message in bytes while the second element is the address
        datafromSocket = sock.recvfrom(2000)
        # Get the actual message
        data = datafromSocket[0].decode()
        # If the message is not the exit code, we are free to proceed with the process
        if data != 'EXIT()':
            # Printing the data received
            print('received "%s"' % data)
            # Client message is logged
            file.write('Client : ' + data)
            file.write('\n')
            # Prints the message received in all caps, and sends it back to the Client
            print(data.upper())
            sock.sendto(data.upper().encode(), datafromSocket[1])
            # Server message is logged
            file.write('Server : ' + data.upper())
            file.write('\n')
        else:
            # When the exit code is entered, the server is informed and then shuts down
            print('The client has requested an end to the session')
            # We write a blank line in order to ensure the log file formats the next message from the client neatly
            file.write('\n')
            # File is then closed.
            file.close()
            # Notice from server stating that the message has been logged to a file
            print('This chat has been logged to a file')
            print('Check client_output.txt to see the logged chat')
            # Exiting the loop
            break


# now close the socket
print('Closing Server')
sock.close();
