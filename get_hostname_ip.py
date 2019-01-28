# Python3 code to display hostname and 
# IP address
# https://www.geeksforgeeks.org/display-hostname-ip-address-python/ 
  
# Importing socket library 
import socket 
  
# Function to display hostname and 
# IP address


def get_host_name_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name, host_ip
    except:
        print("Unable to get Hostname and IP")
  

if __name__ == "__main__":
    # Driver code
    hostname, host_ip = get_host_name_ip()  # Function call

    print("Hostname :  ", hostname)
    print("IP : ", host_ip)
