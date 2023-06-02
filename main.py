import requests, os, re # "requests" needs to be pip installed!

######################
# CONFIGURATION VARS #
######################
API_KEY = "API_KEY_HERE" # You can register yourself a FREE API key here: https://ipapi.com/signup/free

def ConsoleClear():
    os.system('cls' if os.name=='nt' else 'clear')

def get_ip_info(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def validate_ipv4(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, ip)

def IPInfo():
    ConsoleClear()
    print("+------------------------+\n|     IP-Information     |\n|       Mode: IPv4       |\n| Developed by TCSMasked |\n+------------------------+")
    while True:
        ip_address = input("[IPv4] Enter an IP-Address: ")
        if validate_ipv4(ip_address):
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("+------------------------+\n|     IP-Information     |\n|       Mode: IPv4       |\n| Developed by TCSMasked |\n+------------------------+")
            print("Seems like you have tried entering an incorrect IPv4 Address, Please check the IP-Address your trying to query and try again.")
    ip_info = get_ip_info(ip_address)
    if ip_info:
        for key, value in ip_info.items():
            ConsoleClear()
            print("+------------------------+\n|     IP-Information     |\n|       Mode: IPv4       |\n| Developed by TCSMasked |\n+------------------------+")
            print(f"Here is all the available data for the IPv4 Address: {ip_address}")
            print(f"Continent: {ip_info['continent_name']}")
            print(f"Country: {ip_info['country_name']}")
            print(f"Region: {ip_info['region_name']}")
            print(f"City: {ip_info['city']}")
            print(f"Latitude: {ip_info['latitude']}")
            print(f"Longitude: {ip_info['longitude']}")
    else:
        ConsoleClear()
        print("+------------------------+\n|     IP-Information     |\n|       Mode: IPv4       |\n| Developed by TCSMasked |\n+------------------------+")
        print("Unable to fetch IP information.")

def WebInfo():
    #print("+------------------------+\n|     IP-Information     |\n|      Mode: Domain      |\n| Developed by TCSMasked |\n+------------------------+")
    ConsoleClear()
    print("We're sorry, the module you have requested is still being developed.")

def StartPrompt():
    ConsoleClear()
    print("+------------------------+\n|     IP-Information     |\n| Developed by TCSMasked |\n+------------------------+\n\nPlease input which type of IP-Info grabber you would like.\n[A] IPv4 Address Grabber\n[B] Website Information Grabber")
    userInputOne = input("> ")
    if userInputOne == "A":
        IPInfo()
    elif userInputOne == "B":
        WebInfo()
    else:
        StartPrompt()

StartPrompt()
