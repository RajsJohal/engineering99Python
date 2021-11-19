#if_statements
#Indentation is key!
# age = 13

# if age >= 15:
#     print("You can watch this movie")
# else:
#     print("Come back when your older")

film_rating = "18"
# U, PG, 12, 12A, 15, 18
#use if-elif syatemenst to pring appropriate description of the movie
#e.g U ---> Suitable for all ages

if film_rating.upper() == "U":
    print("Suitable for all ages")
elif film_rating == "PG":
    print("Parental guidance is advised")
elif film_rating == "12" or film_rating == "12A": #Could also write film_rating in ("12", "12A")
    print("Suitable for ages 12 and over")
elif film_rating == "15":
    print("Suitable for ages 15 and over")
elif film_rating == "18":
    print("Suitable for ages 18 and over")
else:
    print("Check film rating certificate")