# from the socket module import all
from socket import *
# from the datetime module import all - This is used to get info regarding time and date
from datetime import *
# Create a UDP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)

# Greeting for user using the client
print('Welcome to the UDP Server tester')
print('Use to send messages to a UDP server. Type EXIT() when done')
# Python function used in order to ensure a connection to the server
# without a crash
def connect():
    try:
        # Acquires the host name and IP address from user input using input
        host_name = input('Please enter the name of the host that you want to connect to, or type E to exit :: ')
        # Exit requested, we return -1 to indicate that the exit is inputted
        if host_name == 'E' or host_name == 'e':
            return '-1', '-1'
        IP_address = gethostbyname(str(host_name))
        # Return the host name and address so they can be used later
        return str(host_name), IP_address
    except:
        # In the event where the user fails to make a connection
        # print an error message
        print('ERROR: Failed to connect.')

        # Call the connect method so the user can connect again
        return connect()

# Get the host name and IP address using the previously created method.
host_name, IP_address = connect()
# Check to see if the exit code is inputted
if host_name != '-1':
    # Prints the Host name and IP address to the console
    print('Host name is :: ' + host_name)
    print('IP address :: ' + IP_address)
    try:
        #Need a forever while loop in order to allow the client to talk to the server
        while True:
            # Ask for user to input a message into the console, and then send that message.
            message = input('Enter a message to send to the server :: ')
            print('sending "%s"' % message)
            # Data is transmitted to the server with sendto()
            server_address = (IP_address, 10000)
            sock.sendto(message.encode(), server_address)
            # If the server wants to exit, we inform the user that he/she has requested an end to the session
            # and then we exit the loop
            if message == 'EXIT()':
                print('You have requested an end to the session')
                print('Exiting program')
                break
            # Once message is sent to the server, the client awaits a response
            print('Awaiting response from the server')
            # Look for the response
            amount_received = 0
        	# Data is read from the connection with recv()
            # decode() function returns string object
            data = sock.recv(2000).decode()
            amount_received += len(data)
            # Get the current date and time
            date = datetime.today().strftime("%B %d, %Y")
            time =  datetime.now().strftime("%H:%M:%S")
            # print data received from the server, and the time and date the client got the data
            print('received "%s" on %s at %s' % (data, date, time))

    finally:
        # Close the socket
        print('closing socket')
        sock.close()
else:
    # Inform that the exit code has been entered. 
    print('The exit code has been entered')
    print('closing socket')
    sock.close()
