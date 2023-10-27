import os
import time
import json
import socket
import platform

try:
    import requests
    print("'requests' installed.")
except ImportError:
    print("Installing 'requests'...")
    os.system('pip install requests')

try:
    from whois import whois
    print("'python-whois' installed.")
except ImportError:
    print("Installing 'python-whois'...")
    os.system('pip install python-whois')

author = 'memb3r'
version = '1.0 Beta'

def banner():
    print('''
##      ## ######## ########  ########   #######  ##     ## ######## ########  
##  ##  ## ##       ##     ## ##     ## ##     ## ##     ## ##       ##     ## 
##  ##  ## ##       ##     ## ##     ## ##     ## ##     ## ##       ##     ## 
##  ##  ## ######   ########  ########  ##     ## ##     ## ######   ########  
##  ##  ## ##       ##     ## ##   ##   ##     ##  ##   ##  ##       ##   ##   
##  ##  ## ##       ##     ## ##    ##  ##     ##   ## ##   ##       ##    ##  
 ###  ###  ######## ########  ##     ##  #######     ###    ######## ##     ## 
''')

def warnings():
    while True:
        warning = input('Do you want to clean screen? (Y/n): ')
        if (warning == 'y' or warning == 'Y'):
            os.system('clear')
            break
        elif (warning == 'n' or warning == 'N'):
            break
        elif (warning == ''):
            print(f'This answer is not exist. Try again.')
        else:
            print(f'Answer "{warning}" is not exist. Try again')

def checking():
    print(f'Detecting OS name...')
    time.sleep(1)
    osname = platform.system()
    print(f'{osname} detected.')
    print(f'Checking internet connection stability...')
    time.sleep(2)
    try:
        socket.create_connection(("www.google.com", 80))
        print("Internet connection is stable.")
    except OSError:
        print("Internet connection is unstable.")
    print(f'Starting...')
    time.sleep(1.5)

def start():
    banner()
    print(f'''Author: {author}
Version" {version}

1   >   WHOIS Lookup
2   >   Domain to IP
3   >   IP Geolocation Finder
4   >   IP to Domain
5   >   Port Scanner''')
    while True:
        answer = input('Answer: ')
        if (answer == '1'):
            whoislookup()
        elif (answer == '2'):
            domaintoip()
        elif (answer == '3'):
            ipgeo()
        elif (answer == '4'):
            iptodomain()
        elif (answer == '5'):
            portscan()
        elif (answer == '6'):
            check_domain()
        elif (answer == ''):
            print('This answer is not exist.')
        else:
            print(f'Answer "{answer}" is not exist.')

def whoislookup():
    domain = input('Domain name or IP: ')
    try:
        w = whois(domain)
        print(w)
    except socket.gaierror:
        print("Invalid domain name")
    except Exception as e:
        print(f"Error: {e}")

def domaintoip():
    domain = input('Domain name: ')
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        return "Invalid domain name"
    print(f"The IP address for {domain} is {ip}")

def ipgeo():
    ip_address = input('Enter IP: ')
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print(result)

def iptodomain():
    ip = input('Enter IP: ')
    try:
        domain = socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        try:
            domain = socket.gethostbyaddr(socket.gethostbyname(socket.gethostbyaddr(ip)[0]))[0]
        except (socket.herror, socket.gaierror):
            domain = "No domain associated with this IP"
    print(domain)

def portscan():
    target = input('Enter IP: ')
    start_port = int(input('Enter the port from which we will start: '))
    end_port = int(input('Enter the port from which we will end: '))
    for port in range(start_port, end_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((target, port))
            print('Port ' + str(port) + ' is open')
            s.close()
        except:
            pass

if __name__ == '__main__':
    banner()
    warnings()
    checking()
    start()