from website_text_scraper import *
from known_kanji import *
from prev_search import *
from util import *


def main():
    unique_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}
    kanji_count = [0, 0, 0, 0, 0]
    known_kanji_count = [0, 0, 0, 0, 0]
    known_kanji = get_known_kanji()
    unknown_kanji = {"N5": set(), "N4": set(), "N3": set(), "N2": set(), "N1": set()}

    while True:
        while True:
            print("Enter URL: ")
            url = input()
            print()
            try:
                reset_unique_kanji(unique_kanji)
                reset_kanji_count(kanji_count)

                get_kanji(
                    url,
                    kanji_count,
                    unique_kanji,
                    known_kanji,
                    known_kanji_count,
                    unknown_kanji,
                )
                if (
                    kanji_count[0] == 0
                    and kanji_count[1] == 0
                    and kanji_count[2] == 0
                    and kanji_count[3] == 0
                    and kanji_count[4] == 0
                ):
                    print("URL does not contain any kanji.")
                    print()
                    continue
            except Exception:
                print("Invalid URL")
                print()
                continue
            break

        update_prev_search_table(url, kanji_count)

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
                print_reading_ability(kanji_count, known_kanji_count)
            if i == "2":
                print_unknown_kanji(unknown_kanji)
            if i == "3":
                all_time_total = get_all_time_total()
                print_all_time_total(all_time_total)
            if i == "4":
                break
            if i == "5":
                return


if __name__ == "__main__":
    main()