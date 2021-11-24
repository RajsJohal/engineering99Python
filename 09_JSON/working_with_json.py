import json

with open("demo.json") as jsonfile:
    read_file = jsonfile.read()
    print(read_file, type(read_file))
    demo = json.loads(read_file)
    print(demo)
    print(type(demo))

    print(demo["Objects"]["Key"]) #["Key"] when trying to access key value pair

#create a python dictionary
#with info about
#your fav film/tv series

show = {
    "Show Name": "Mr.Robot",
    "Director": "Sam Esmail",
    "Lead Actor": "Rami Malik",
    "No. of Seasons": 4,
    "Perfect": True,
    "flaws": None
}

show["Genre"] = "Drama, Psychological Thriller, Techno-Thriller"
show["Release Year"] = 2015
print(show)

show_json_string = json.dumps(show) # convert to a string json
print(show_json_string)
print(type(show_json_string))

#with open("show.json", "w") as showfile:
#   showfile.write(show_json_string)

with open("1show.json", "w") as oneshowfile:
    json.dump(show, oneshowfile) # dump skips the step to create a json file and does it all in one