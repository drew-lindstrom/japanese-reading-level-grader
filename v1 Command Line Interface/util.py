def print_count(kanji_count, total):
    """Prints the number of kanji in each JLPT level and percentage of said kanji out of total count."""
    print(f"Total Number of Characters: {total}")
    print(f"N5: {kanji_count[0]} ({str(round((kanji_count[0]/total), 4)*100)}%)")
    print(f"N4: {kanji_count[1]} ({str(round((kanji_count[1]/total), 4)*100)}%)")
    print(f"N3: {kanji_count[2]} ({str(round((kanji_count[2]/total), 4)*100)}%)")
    print(f"N2: {kanji_count[3]} ({str(round((kanji_count[3]/total), 4)*100)}%)")
    print(f"N1: {kanji_count[4]} ({str(round((kanji_count[4]/total), 4)*100)}%)")
    print()


def print_unique_count(unique_kanji, unique_total):
    """Prints the number of unique kanji in each JLPT level and percentage of said kanji out of total unique count."""
    print(f"Total Number of Unique Characters: {unique_total}")
    print(
        f"N5: {len(unique_kanji['N5'])} ({str(round((len(unique_kanji['N5'])/unique_total), 4)*100)}%)"
    )
    print(
        f"N4: {len(unique_kanji['N4'])} ({str(round((len(unique_kanji['N4'])/unique_total), 4)*100)}%)"
    )
    print(
        f"N3: {len(unique_kanji['N3'])} ({str(round((len(unique_kanji['N3'])/unique_total), 4)*100)}%)"
    )
    print(
        f"N2: {len(unique_kanji['N2'])} ({str(round((len(unique_kanji['N2'])/unique_total), 4)*100)}%)"
    )
    print(
        f"N1: {len(unique_kanji['N1'])} ({str(round((len(unique_kanji['N1'])/unique_total), 4)*100)}%)"
    )
    print()


def print_reading_ability(kanji_count, known_kanji_count):
    """Prints number and percentage of known kanji out of number of kanji per JLPT level. Does not include unique kanji."""
    print(
        f"N5: {known_kanji_count[0]} out of {kanji_count[0]} known. ({str(round((known_kanji_count[0]/kanji_count[0]), 4)* 100)}%)"
    )
    print(
        f"N5: {known_kanji_count[1]} out of {kanji_count[1]} known. ({str(round((known_kanji_count[1]/kanji_count[1]), 4)* 100)}%)"
    )
    print(
        f"N5: {known_kanji_count[2]} out of {kanji_count[2]} known. ({str(round((known_kanji_count[2]/kanji_count[2]), 4)* 100)}%)"
    )
    print(
        f"N5: {known_kanji_count[3]} out of {kanji_count[3]} known. ({str(round((known_kanji_count[3]/kanji_count[3]), 4)* 100)}%)"
    )
    print(
        f"N5: {known_kanji_count[4]} out of {kanji_count[4]} known. ({str(round((known_kanji_count[4]/kanji_count[4]), 4)* 100)}%)"
    )
    print()


def print_all_time_total(all_time_total):
    """Prints the kanji count for each JLPT level for all previous valid searches."""
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


def print_unknown_kanji(unknown_kanji):
    """Prints kanji from URL that are not in known_kanji by JLPT level."""
    print("Unknown Kanji:")
    print()

    print("JLPT N5: ")
    print()
    for kanji in unknown_kanji["N5"]:
        print(kanji)
    print()

    print("JLPT N4: ")
    print()
    for kanji in unknown_kanji["N4"]:
        print(kanji)
    print()

    print("JLPT N3: ")
    print()
    for kanji in unknown_kanji["N3"]:
        print(kanji)
    print()

    print("JLPT N2: ")
    print()
    for kanji in unknown_kanji["N2"]:
        print(kanji)
    print()

    print("JLPT N1: ")
    print()
    for kanji in unknown_kanji["N1"]:
        print(kanji)
    print()


def get_total(kanji_count):
    """Retrieves total number of kanji from URL."""
    total = 0

    for count in kanji_count:
        total += count

    return total


def get_unique_total(unique_kanji):
    """Retrieves total number of unique kanji from URL."""
    unique_total = 0

    for key in unique_kanji:
        unique_total += len(unique_kanji[key])

    return unique_total


def reset_unique_kanji(unique_kanji):
    """Resets unique kanji count. To be used before each URL search."""
    unique_kanji["N5"] = set()
    unique_kanji["N4"] = set()
    unique_kanji["N3"] = set()
    unique_kanji["N2"] = set()
    unique_kanji["N1"] = set()


def reset_kanji_count(kanji_count):
    """Resets kanji count. To be used before each URL search."""
    for level in range(len(kanji_count)):
        kanji_count[level] = 0
