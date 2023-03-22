import os
from fpdf import FPDF


class TxtToPdf:
    def __init__(self, txt_file):
        self.converter = FPDF()
        self.file = txt_file
        self.__file_converter()

    def __file_converter(self):

        if not os.path.exists(self.file):
            f = open(self.file, "w")
            f.close()
        else:
            print("File Exists")
        self.converter.output(self.file + ".pdf")
        try:
            os.rename(self.file + ".pdf", "output.pdf")
        except:
            print("already file exits")

    def get_file_contents(self):
        with open("output.pdf", "r") as f:
            return f.read()

    def __del__(self):
        try:
            if os.path.exists(self.file):
                os.remove(self.file)
            if os.path.exists("output.pdf"):
                os.remove("output.pdf")
        except:
            print(f"{self.file} does not exist.")
        else:
            print(f"{self.file} file deleted successfully.")
if __name__ == "__main__":
    obj = TxtToPdf("txt")
    file = obj.get_file_contents()
    print(type(file))
    del obj
