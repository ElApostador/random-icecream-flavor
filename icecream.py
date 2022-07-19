import random
def primary():
   print("the flavor of the week is.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()
   last= 63
   rnd = random.randint(0, last)
   print (quotes[rnd]*1)

if __name__== "__main__":
  primary()
