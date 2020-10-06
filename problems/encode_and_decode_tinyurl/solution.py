from random import randint

class Codec:
    STANDARD_LENGTH = 6
    BASE_URI = 'https://tinyurl.com/'
    def __init__(self):
        self.url_db = {}
        

    def generate_random_string(self, longUrl:str):
        # actually come up with a random string for this!
        return ''.join([chr(randint(65,90)) for n in range(6)])
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        rand_string = self.generate_random_string(longUrl)
        while rand_string in self.url_db.keys():
            rand_string = self.generate_random_string(longUrl)
             
        self.url_db[rand_string] = longUrl
        
        return f'{self.BASE_URI}{rand_string}'
        
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        suffix = shortUrl.split('/')[-1]
        originalUrl = self.url_db.get(suffix)
        return originalUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

