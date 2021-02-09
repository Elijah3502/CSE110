#get file

book = ""
chapters = -1
scripture = ""

chapter_max = -1
book_max = ""
with open("/Users/elijah/BYUI/Programming Building Blocks/Week 6/books_and_chapters.txt") as books_chapters:
    for line in books_chapters:
        parts = line.split(":")

        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()

        print(f"Scripture: {scripture}, Book: {book}, Chapter: {chapters}")

        if chapters > chapter_max:
            chapter_max = chapters
            book_max = book

            
print(f"The book with the most chapters in the scriptures is {book_max}")
print(f"The most number of chapters is : {chapter_max}")










#scripture of chapters

#book most chapters