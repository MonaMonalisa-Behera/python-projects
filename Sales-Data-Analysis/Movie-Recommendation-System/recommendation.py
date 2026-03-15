movies = ["Avatar", "Titanic", "Avengers", "Inception", "Interstellar"]

user_choice = "Avatar"

print("Because you watched:", user_choice)
print("Recommended movies:")

for movie in movies:
    if movie != user_choice:
        print(movie)
