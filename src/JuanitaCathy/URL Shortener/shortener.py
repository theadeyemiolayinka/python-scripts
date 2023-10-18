import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

if __name__ == "__main__":
    long_url = input("Enter the long URL: ")

    short_url = shorten_url(long_url)
    print("Shortened URL:", short_url)
