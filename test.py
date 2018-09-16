def SayHello(name):
    print("I want to sayy hello with you, {0}".format(name))
    print("Hello, {0}".format(name))
    print("Done")

if __name__ == "__main__":
    print("***" * 10)
    name = input("Pleast input your name:")
    print(SayHello(name = name))
    print("@@@" * 10)

