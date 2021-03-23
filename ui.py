from website_text_scraper import parse_text


def print_count(kanji_count):
    print(f"Number of JLPT N5 Characters: {kanji_count[0]}")
    print(f"Number of JLPT N4 Characters: {kanji_count[1]}")
    print(f"Number of JLPT N3 Characters: {kanji_count[2]}")
    print(f"Number of JLPT N2 Characters: {kanji_count[3]}")
    print(f"Number of JLPT N1 Characters: {kanji_count[4]}")
    print()


def print_count_unique(unique_kanji):
    print(f"Number of Unique JLPT N5 Characters: {len(unique_kanji['N5'])}")
    print(f"Number of Unique JLPT N4 Characters: {len(unique_kanji['N4'])}")
    print(f"Number of Unique JLPT N3 Characters: {len(unique_kanji['N3'])}")
    print(f"Number of Unique JLPT N2 Characters: {len(unique_kanji['N2'])}")
    print(f"Number of Unique JLPT N1 Characters: {len(unique_kanji['N1'])}")
    print()


print("Enter URL: ")
url = input()

print_count(kanji_count)
print_count_unique(unique_kanji)