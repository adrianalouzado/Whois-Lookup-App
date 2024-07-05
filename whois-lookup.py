import socket

def whois_lookup(domain: str): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()
    return response


def main():
    print("Whois Lookup App")
    while True:
        domain = input("Enter a domain or type 'exit' to quit: ")
        if domain.lower() == 'exit':
            print("Exiting the Whois Lookup App")
            break
        response = whois_lookup(domain)
        print(f"Whois information for {domain}:\n{response}\n")
if __name__ == "__main__":
    main()

