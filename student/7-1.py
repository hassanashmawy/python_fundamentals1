
doc = "The Story of GOD"
comedy = "Last Vegas"
drama = "Shawshank Redemption"
dramedy = "The Bucket List"
alt_book = "5 seconds rule"

  
print("What kind of movies you like?")
print("1. Documentaries")
print("2. Dramas")
print("3. Comedies")
print("Type the number you like - If you like more than one, just type both like 123 if you like them all!")
print("If you not into movies just type No")

fav = input()
message = "" # "You are really not into movies, maybe you like this book: {}".format(alt_book)

print()

if fav.find('1') >= 0 :
    message += "Documentaries! great maybe you can enjoy {} by Morgan Freeman \n".format(doc)
if fav.find('2') >= 0 and fav.find('3') >= 0:
    message += "Dramas and Comedies!! you can enjoy {} by Morgan Freeman \n".format(dramedy)
elif fav.find('2') >= 0:
    message += "Dramas! you can enjoy {} by Morgan Freeman \n".format(drama)
elif fav.find('3') >= 0:
    message += "Comedies! you can enjoy {} by Morgan Freeman \n".format(comedy)
if fav.casefold() == "no":
    message = "You are really not into movies, maybe you like this book: {}".format(alt_book)


print(message)
