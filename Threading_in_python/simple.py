from threading import Thread


def display():
    for i in range(10):
        print("Ankush")
    print()


def Display_two():
    for i in range(10):
        print("Anish")
    print()


t1 = Thread(target=display)
print(t1.is_alive())


t2 = Thread(target=Display_two)

t2.start()
# t1.start()
print(t2.is_alive())
