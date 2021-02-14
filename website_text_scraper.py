from kanji_dict import kanji_dict
import requests
import urllib.request

url = "https://ja.wikipedia.org/wiki/Al-Amal"

uf = urllib.request.urlopen(url)
html = uf.read()


decode_hex = codecs.getdecoder("hex_codec")


# for a string
string = decode_hex(html)[0]