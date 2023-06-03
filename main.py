import requests, os, re, whois, dns.resolver

######################
# CONFIGURATION VARS #
######################
API_KEY = "API_KEY_HERE" # You can register yourself a FREE API key here: https://ipstack.com/signup/free

def ConsoleClear():
    os.system('cls' if os.name=='nt' else 'clear')

def get_dns_records(domain):
    records = []
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA']
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for rdata in answers:
                records.append((record_type, str(rdata)))
        except dns.resolver.NoAnswer:
            continue
    return records

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
    ConsoleClear()
    print("+------------------------+\n|     IP-Information     |\n|      Mode: Domain      |\n| Developed by TCSMasked |\n+------------------------+")
    while True:
        domain = input("Enter a domain name: ")
        if domain:
            break
        else:
            print("Invalid domain name. Please try again.")
    try:
        w = whois.whois(domain)
        dns_records = get_dns_records(domain)
        ConsoleClear()
        print("+------------------------+\n|     IP-Information     |\n|      Mode: Domain      |\n| Developed by TCSMasked |\n+------------------------+")
        print(f"Here is the information for the domain: {domain}")
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Registration Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
        print("DNS Records:")
        for record_type, record_data in dns_records:
            print(f"Type: {record_type}, Data: {record_data}")
    except whois.parser.PywhoisError as e:
        ConsoleClear()
        print("+------------------------+\n|     IP-Information     |\n|      Mode: Domain      |\n| Developed by TCSMasked |\n+------------------------+")
        print(f"Unable to fetch information for the domain: {domain}")
        print(f"Error: {e}")

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
