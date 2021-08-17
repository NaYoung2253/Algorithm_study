import sys 
from collections import Counter

N = int(sys.stdin.readline())
books = []
for i in range(N):
    books.append(sys.stdin.readline().strip('\n'))

sort_book = sorted(books)
mode_count = Counter(sort_book)
most_book = mode_count.most_common()

print(most_book[0][0])