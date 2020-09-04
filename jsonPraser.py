import os
import json
import codecs


single = {
    "name": "Here Comes The Sun",
    "artist" : "The Beatles",
    "genre" : "Pop",
    "country": "US-UK"
}

with codecs.open("answers.json",'a','utf8') as f:
    while True:
        genre = input("genre: ")
        times = int(input("quantity: "))
        for i in range(times):
            country = input("country: ")
            quan = int(input("quantity: "))
            for j in range(quan):
                artist = input("artist: ")
                names = input("Hello: ").split(', ')
                for name in names:
                    # name = input("name: ")
                    single["name"] = name
                    single["artist"] = artist
                    single["genre"] = genre
                    single["country"] = country
                    f.write(json.dumps(single,ensure_ascii=False))
                    f.write(",\n")