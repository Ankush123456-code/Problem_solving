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

class Signer:
    Sign = {
        "cse": ["cs"],
        "mech": ["mech", "mech_ece"]
    }

    @classmethod
    def get(cls, attr):
        return cls.Sign.get(attr)


print(Signer.get("mech")[0])
