from website_text_scraper import parse_text, get_kanji
from known_kanji import get_known_kanji
from prev_serach import update_prev_search_db, get_all_time_total


def print_count(kanji_count, total):
    print(f"Total Number of Characters: {total}")
    print(f"N5: {kanji_count[0]} ({round((kanji_count[0]/total), 4)*100}%)")
    print(f"N4: {kanji_count[1]} ({round((kanji_count[1]/total), 4)*100}%)")
    print(f"N3: {kanji_count[2]} ({round((kanji_count[2]/total), 4)*100}%)")
    print(f"N2: {kanji_count[3]} ({round((kanji_count[3]/total), 4)*100}%)")
    print(f"N1: {kanji_count[4]} ({round((kanji_count[4]/total), 4)*100}%)")
    print()


def print_unique_count(unique_kanji, unique_total):
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


def print_all_time_total(all_time_total):
    total = 0
    for level in all_time_total[0]:
        total += level

    print(f"Total Number of Characters: {total}")
    print(f"N5: {all_time_total[0][0]}")
    print(f"N4: {all_time_total[0][1]}")
    print(f"N3: {all_time_total[0][2]}")
    print(f"N2: {all_time_total[0][3]}")
    print(f"N1: {all_time_total[0][4]}")
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


def reset_unqiue_kanji():
    unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}


def reset_kanji_count():
    kanji_count = [0, 0, 0, 0, 0]


unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}
kanji_count = [0, 0, 0, 0, 0]

# TODO: Message for websites without any kanji
# TODO: prev_serach db shouldn't update with websites without kanji
# TODO: unique_kanji and kanji_count need to reset with each URL search
# TODO: Rounding error


def main():
    while True:
        while True:
            print("Enter URL: ")
            url = input()
            print()
            try:
                get_kanji(url, kanji_count, unique_kanji)
            except Exception:
                print("Invalid URL")
                print()
                continue
            break

        update_prev_search_db(url, kanji_count)

        total = get_total(kanji_count)
        unique_total = get_unique_total(unique_kanji)

        print_count(kanji_count, total)
        print_unique_count(unique_kanji, unique_total)

        while True:
            print(
                "(1) Print Reading Ability of URL, (2) Print Unknown Kanji from URL, (3) Print Total Number of Kanji from All Previous Searches, (4) Enter New URL, (5) Quit"
            )
            i = input()
            print()

            if i == "1":
                pass
            if i == "2":
                pass
            if i == "3":
                all_time_total = get_all_time_total()
                print_all_time_total(all_time_total)
            if i == "4":
                break
            if i == "5":
                return


if __name__ == "__main__":
    main()