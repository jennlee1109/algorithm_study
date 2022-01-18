n = int(input())
books = dict()

max_val = 0
for i in range(n):
    name = input()
    if name not in books:
        books[name] = 1
    else:
        books[name] += 1
    if max_val < books[name]:
        max_val = books[name]

sorted_books = sorted(books.items(), key=lambda x:(x[1], x[0]))

for name, count in sorted_books:
    if count == max_val:
        print(name)
        break

# print(sorted_books)