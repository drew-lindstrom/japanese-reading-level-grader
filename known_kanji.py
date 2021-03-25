def get_known_kanji():
    f = open("Known_Kanji.txt", "r")

    known_kanji = set()

    for character in f:
        known_kanji.add(character)

    return known_kanji