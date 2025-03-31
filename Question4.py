class IPException(Exception):
    def __init__(self, ipAddress):
        self.ip_address = ipAddress
        super().__init__(f"Invalid IP address: {ipAddress}")
    def check(ip):
        passable = "0123456789."
        for character in ip:
            if character not in passable:
                raise IPException(ip)

credentials = []
def info():
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        ipAddress = input("Enter your IP Address: ")
        IPException.check(ipAddress)


        addInfo = [username,password,ipAddress]
        credentials.append(addInfo)

        with open("SessionLogger.txt", "a") as file:
            file.write(str(addInfo) + "\n")
            print("Your info has been saved.")

    except IPException as error:
        print("There was an error.", error)

if __name__ == "__main__":
    info()
