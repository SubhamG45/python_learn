books=[ "bookA","bookB","bookC","bookD"]
for book in books:
    if book== "bookC":
        print("found the book! stop searching.")
        break
    print(f"checking {book}")
print("serach ended.")