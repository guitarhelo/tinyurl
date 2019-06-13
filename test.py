from ShortURLGenerator import ShortURLGenerator

idgen = ShortURLGenerator(8).generate_id()
short_url=ShortURLGenerator(8).generate_short_url("https://www.amazon.com")
print(short_url)