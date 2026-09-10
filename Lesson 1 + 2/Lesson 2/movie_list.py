movie1 = input("Enter a movie name guess: ")
movie2 = input("Enter a movie name guess: ")
movie3 = input("Enter a movie name guess: ")
movie4 = input("Enter a movie name guess: ")
movie5 = input("Enter a movie name guess: ")

movie_list = [movie1, movie2, movie3, movie4, movie5]
new_list = []
for movie in movie_list:
    if movie.lower() == "frozen":
        new_list.append(movie)
if new_list:
    print("Correct, u guessed ", new_list)
else:
    print("Nope, no correct guesses.")