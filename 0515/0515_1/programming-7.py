class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile="", office="", email=""):
        self.contacts[name] = {"mobile": mobile, "office": office, "email": email}

    def __str__(self):
        result = ""

        for name in self.contacts:
            info = self.contacts[name]

            result = result + name + "\n"

            if info["office"]:
                result = result + "office phone:   " + info["office"] + "\n"

            if info["email"]:
                result = result + "email address:  " + info["email"] + "\n"

            result = result + "\n"

        return result.strip()


obj = PhoneBook()

obj.add("Kim", office="1234567", email="kim@company.com")
obj.add("Park", office="2345678", email="park@company.com")

print(obj)

# p403 7번 문제