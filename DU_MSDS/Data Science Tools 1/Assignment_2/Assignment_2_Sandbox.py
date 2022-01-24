import string

class CaesarCipher:

    def __init__(self, key=3):
        self.key = key % 26
        self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key]))

        # Dict used for encryption
        self.e.update(dict(zip(string.ascii_uppercase, string.ascii_uppercase[self.key:] + string.ascii_lowercase[:self.key])))


        # Dict used for decryption
        self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key], string.ascii_lowercase))
        self.d.update(dict(zip(string.ascii_uppercase[self.key:] + string.ascii_uppercase[:self.key], string.ascii_uppercase)))

    def encrypt(self, plaintext):
        return ''.join([self.e[letter] if letter in self.e else letter for letter in plaintext])

    def decrypt(self, ciphertext):
        return ''.join([self.d[letter] if letter in self.d else letter for letter in ciphertext])


sentence2Cipher = "there is a quiz tomorrow"

test = CaesarCipher(3)
test.encrypt(sentence2Cipher)