import unittest
import string


# ---------------------------------------
# PRODUCTION CODE
# ---------------------------------------
def encrypt(message):
    # create alphabet
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    # use alphabet to encrypt the message
    encrypted_message = "".join(
        [abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
    return encrypted_message


# ---------------------------------------
# UNIT TESTS
# ---------------------------------------
class TestEncryption(unittest.TestCase):
    # -- demo message --
    def setUp(self):
        self.my_message = "banana"

    # -- 1. is there a message to encrypt? --
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    # -- 2. is the input message a string? --
    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    # -- 3. does the function encrypt() accept input and return output? --
    def test_functReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

    # -- 4. do the input and output messages have the same length? --
    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    # -- 5. is the input message not revealed within the output? --
    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message))

    # -- 6. is the output message a string? --
    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str)

    # -- 7. is the output message encrypted via Caesars Cipher? --
    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join(
            [abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in
             enumerate(self.my_message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message))


if __name__ == "__main__":
    unittest.main()
