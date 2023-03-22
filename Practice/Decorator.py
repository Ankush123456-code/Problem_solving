def welcome(func):
    def hello():
        print("I am Ankhs from Inner Function")  # added new Functionality
        func()  # existing functionality
        print("after func ")  # added new functionality

    return hello


@welcome
def Hello_world():
    print("hello world")


# hello_world = welcome(Hello_world)
Hello_world()
