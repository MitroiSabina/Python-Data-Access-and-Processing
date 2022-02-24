from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.test

# title = input("Enter movie title: ")
# genre = input("Enter movie genre: ")
# year = input("Enter movie year: ")

movies = db.movies

# movie_details = [
#     { 'title': title,
#       'genre': genre,
#       'year': year
#       }
# ]
#
# movies.insert_one(movie_details)

movie_details = [
    { 'title': 'Shutter Island', 'genre': 'Thriller', 'year': 2010},
    { 'title': 'The King\'s Man', 'genre': 'Trailer', 'year': 2021},
    { 'title': 'Skyfall', 'genre': 'Action', 'year': 2012},
    { 'title': 'Dog', 'genre': 'Comedy', 'year': 2022},
    { 'title': 'The Invisible Man', 'genre': 'Trailer', 'year': 2020},
    { 'title': 'Swallow', 'genre': 'Trailer', 'year': 2019},
]

movies.insert_many(movie_details)

result = movies.find()

for r in result:
    print("Title: {} | Genre: {} | Year: {}".format(r['title'], r['genre'], r['year']))