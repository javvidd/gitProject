# homework
# chapter 8-1 to 8-5

def display_message():
    print("im learning chapter 8 functions")
display_message()


def favourite_book(title):
    print(f"one of my favourite books is {title.title()}")
favourite_book("alice in wonderland")


def make_shirt(size, text):
    print(f"customised shirt is \"{size.upper()}\" size with printed \"{text.upper()}\" words")
make_shirt("L", "Def x():")
make_shirt(text="hello world", size="m")

def make_shirt_2(text, size="l"):
    print(f"customised shirt is \"{size.upper()}\" size with printed \"{text.upper()}\" words")
make_shirt_2(text="we all r in love")
make_shirt_2("i luv python", "m")

def describe_city(city, country="USA"):
    print(f"{city.title()} is in {country.capitalize()}")
describe_city("baku", "azerbaijan")
describe_city("boston")
describe_city("london", "england")


# chapter 8-6
def city_country(city, country):
    return f"\'{city}\', \'{country}\'"
pair = city_country("baku", "azerbaijan")
pair2 = city_country("newyork", "usa")
pair3 = city_country("paris", "france")
print(pair + "\n" + pair2 + "\n" + pair3)


def make_album(artist, al_title, track_num=""):
    if track_num:
        return {"name": artist , "album": al_title, "number": track_num}
    else:
        return {"name": artist, "album": al_title}

print(f'{make_album("uzeir", "esgerliy")}\n{make_album("madonna", "bayatishiraz", 5)}\n{make_album("namig", "garachuxurlu", 4)}')