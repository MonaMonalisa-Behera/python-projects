movies = ["Avatar", "Titanic", "Avengers", "Inception"]

user_choice = "Avatar"

print("Because you watched:", user_choice)

for movie in movies:
    if movie != user_choice:
        print("Recommended:", movie)
