#Dictionaries
#Consist of key value pairs, where the key is a refernce to the values

d = {
    "Key": "Value"
}

print(d, type(d))

c = {
    "Course": "Engineering 99",
    "Stream": "DevOps",
    "Number of Trainees": 11,
}

print(c)

#Access a value
print(c["Stream"]) # Returns the value
print(c.get("Stream"))

#Change a value
c.update({"Stream": "Data Eng", "Length_weeks": 8})
print(c)

#Favourite Movie Dictionary

fav_movie = {
    "Title": "Interstellar",
    "Lead_Actor": "Matthew McConaughey",
    "Genre": "Sci-Fi",
    "Budget(USD)": 165000000,
    "Year of Release": 2014,
}



#Differece between get and []
# print(c["Steam"])
# print(c.get("Steam"))
