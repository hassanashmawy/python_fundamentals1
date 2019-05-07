# def highest_rate(doc_rate, dra_rate, com_rate):
#     print(doc_rate, dra_rate, com_rate)
    
doc = "The Story of GOD"
comedy = "Last Vegas"
drama = "Shawshank Redemption"
dramedy = "The Bucket List"
alt_book = "5 seconds rule"

  
print("What kind of movies you like?")
doc_rate = int(input("one to five for ||Documentaries||"))
dra_rate = int(input("one to five for ||Dramas||"))
com_rate = int(input("one to five for ||Comedies||"))

recommend=""

if doc_rate >= 4:
    recommend = "Documentaries!->" + doc
elif dra_rate >= 4 and com_rate >= 4:
    recommend = "Dramas and Comedies!!->" + dramedy
elif dra_rate >= 4:
    recommend = "Dramas!->" + drama
elif com_rate >= 4:
    recommend = "Comedies!->" + comedy
elif doc_rate <= 3 and dra_rate <= 3 and com_rate <= 3:
    recommend = "you love nothing but you may enjoy->"
    if doc_rate > dra_rate and doc_rate > com_rate:
        recommend += doc
    elif dra_rate > doc_rate and dra_rate > com_rate:
        recommend += drama
    elif com_rate > dra_rate and com_rate > doc_rate:
        recommend += comedy
    else:
        recommend += "a book!:" + alt_book    

# highest_rate(doc_rate, dra_rate, com_rate)

print(recommend)
    # pass
# print("Type the number you like - If you like more than one, just type both like 123 if you like them all!")
# print("If you not into movies just type No")
