import re

# Find all numbers in a given string
text = """In 1994, a small village celebrated its 200th anniversary with a gathering of nearly 1,000 people. The event was remarkable not only for its size but also for the stories shared. One farmer spoke of tending 12 sheep, 7 goats, and 3 cows, while another mentioned harvesting 25 bushels of wheat each year since he was 18. Children played games, counting up to 50 before hiding behind 6 large trees that lined the central square.

A historian presented records showing that, in 1821, there were only 48 houses, compared to more than 300 homes in 2025. The population, once 230, had grown steadily, reaching nearly 5,600. He also noted that, during a drought in 1911, families survived by pooling 40 barrels of stored water and 200 loaves of bread.

Musicians entertained the crowd with songs that had been passed down for 4 generations. The rhythm of 2 drums, 1 fiddle, and 1 flute carried through the evening. Food was plentiful: 60 pies, 75 loaves of fresh bread, and 20 roasted chickens.

Later, fireworks lit up the sky for exactly 15 minutes, with bursts numbered from 1 to 12 by enthusiastic children. Visitors traveled from 9 neighboring towns, some covering more than 80 kilometers.

By midnight, when the bells rang 12 times, everyone agreed it had been a day worth remembering. The numbers—big and small—told the story of a community that had grown, endured, and celebrated life together across centuries."""

print(re.findall(r'\d+', text))

""" EXTRA """
# Validate email addresses
def mail_validator(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Validate phone numbers
def phone_validator(phone):
    pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    return re.match(pattern, phone) is not None

# Validate URLs
def url_validator(url):
    pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[\w.-]*)*\/?$'
    return re.match(pattern, url) is not None

def main():
    print(mail_validator("test56@gmail.com"))
    print(mail_validator("test56.gmail.com"))
    print(phone_validator("+34 123-456-789"))
    print(phone_validator("+34 "))
    print(url_validator("https://test56.github.io"))
    print(url_validator("https://test56.github.23"))

if __name__ == "__main__":
    main()