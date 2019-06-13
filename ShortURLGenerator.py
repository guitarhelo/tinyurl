import random
from urllib.parse import urlparse
class ShortURLGenerator(object):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, length=8):
        self._alphabet_length = len(self.ALPHABET)
        self._id_length = length

    def _encode_int(self, n):


        encoded = ''
        while n > 0:
            n, r = divmod(n, self._alphabet_length)
            encoded = self.ALPHABET[r] + encoded
        return encoded

    def generate_id(self):
        """Generate an ID without leading zeros.

        For example, for an ID that is eight characters in length, the
        returned values will range from '10000000' to 'zzzzzzzz'.
        """

        start = self._alphabet_length**(self._id_length - 1)
        end = self._alphabet_length**self._id_length - 1
        return self._encode_int(random.randint(start, end))
    def generate_short_url(self,url):
        input = urlparse(url)
        output=input.scheme+'://'+input.netloc+'/'+self.generate_id()
        return output

if __name__ == "__main__":
    # Sample usage: Generate ten IDs each eight characters in length.
    idgen = ShortURLGenerator(8)

    generateList = []
    for i in range(10):
        print(idgen.generate_id())
        generateList.append(idgen.generate_short_url("https://www.google.com"))

    for j in range(10):
        print(generateList[j])
