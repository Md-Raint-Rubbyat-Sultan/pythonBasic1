def main():
    times = howManyMeow()
    meow(times)

def howManyMeow():
    while True:
        meowTime = int(input("How many time the cat should Meow? "))
        if meowTime >= 0:
            return meowTime  

def meow(n):
    for _ in range(n):
        print("Meow")

main()