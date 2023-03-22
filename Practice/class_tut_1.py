class Journel:
    def __init__(self):
        self.__article = []
        self.__count = 0

    def write_article(self, text):
        self.__article.append(text)
        self.__count += 1

    def print(self):
        print(str(self.__article))

    def get_data(self):
        return self.__article

    # @staticmethod
    # def save_file(filename, con_data):
    #     content = open(filename, 'a')
    #     content.write(str(con_data))
    #     content.close()
    #
    def __str__(self):
        return "\n".join(self.__article)

    def save_file(self,filename):
        content = open(filename, 'w')
        content.write(str(self))
        content.close()
        # print(self)


obj = Journel()
obj.write_article(" hello world ")
obj.write_article(" hello world2 ")
obj.write_article(" hello world3 ")
obj.write_article(" hello world4 ")
file = "journel.txt"
obj.save_file(file)

with open(file) as fh:
    print(fh.read())
