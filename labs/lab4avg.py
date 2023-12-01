# Lab 04 (cont.) - Get the average book price

from lab4books import getAllBooks

books = getAllBooks()
total = 0
count = 0
for book in books:
    total += book["Price"]
    count += 1

avg = round(total/count, 2)

print (f"The average price of {count} books is {avg}")