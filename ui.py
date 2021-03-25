from website_text_scraper import parse_text, get_kanji


def print_count(kanji_count, total):
    print(f"Total Number of Characters: {total}")
    print(f"N5: {kanji_count[0]} ({round((kanji_count[0]/total), 4)*100}%)")
    print(f"N4: {kanji_count[1]} ({round((kanji_count[1]/total), 4)*100}%)")
    print(f"N3: {kanji_count[2]} ({round((kanji_count[2]/total), 4)*100}%)")
    print(f"N2: {kanji_count[3]} ({round((kanji_count[3]/total), 4)*100}%)")
    print(f"N1: {kanji_count[4]} ({round((kanji_count[4]/total), 4)*100}%)")
    print()


def print_count_unique(unique_kanji, unique_total):
    print(f"Total Number of Unique Characters: {unique_total}")
    print(
        f"N5: {len(unique_kanji['N5'])} ({round((len(unique_kanji['N5'])/unique_total), 4)*100}%)"
    )
    print(
        f"N4: {len(unique_kanji['N4'])} ({round((len(unique_kanji['N4'])/unique_total), 4)*100}%)"
    )
    print(
        f"N3: {len(unique_kanji['N3'])} ({round((len(unique_kanji['N3'])/unique_total), 4)*100}%)"
    )
    print(
        f"N2: {len(unique_kanji['N2'])} ({round((len(unique_kanji['N2'])/unique_total), 4)*100}%)"
    )
    print(
        f"N1: {len(unique_kanji['N1'])} ({round((len(unique_kanji['N1'])/unique_total), 4)*100}%)"
    )
    print()


def get_total(kanji_count):
    total = 0

    for count in kanji_count:
        total += count

    return total


def get_unique_total(unique_kanji):
    unique_total = 0

    for key in unique_kanji:
        unique_total += len(unique_kanji[key])

    return unique_total


unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}
kanji_count = [0, 0, 0, 0, 0]

# TODO: Error handling for invalid URL

print("Enter URL: ")
url = input()
print()

get_kanji(url, kanji_count, unique_kanji)
total = get_total(kanji_count)
unique_total = get_unique_total(unique_kanji)
print_count(kanji_count, total)
print_count_unique(unique_kanji, unique_total)