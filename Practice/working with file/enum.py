import enum


# class SignerType(enum.Enum):
#     Mift = ["mi", "mc"]
#     cs = ["cs"]
#
#     @classmethod
#     def get(cls, param):
#         return param
#
#
# print(SignerType["cs"].value[0])

class SignerType:
    SignerType = {
        "cs": ["cs"],
        "mift": ["mift", "cs"]
    }

    @classmethod
    def get(cls, attr):
        return cls.SignerType.get(attr)


print(SignerType.get("mift")[0])
