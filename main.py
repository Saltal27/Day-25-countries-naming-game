import pandas
from scoreboard import Scoreboard
from turtle import Screen

IMAGE = "Map_of_the_Arab_world.gif"

screen = Screen()
screen.title("Arab countries naming game")
screen.bgpic(IMAGE)
screen.setup(width=1025, height=577)

scoreboard = Scoreboard()

countries_data = pandas.read_csv("countries.csv")
countries_names = countries_data["country"].tolist()
countries_x = countries_data["x"].tolist()
countries_y = countries_data["y"].tolist()


correct_guesses = []
while len(correct_guesses) < 20:
    player_answer = screen.textinput(title=f"{scoreboard.score}/21 correct", prompt="Name an arabic country").title()

    if player_answer == "Exit":
        break
    if player_answer in countries_names:
        scoreboard.increase_score()
        country_index = countries_names.index(player_answer)
        country_x = countries_x[country_index]
        country_y = countries_y[country_index]
        scoreboard.write_country_name(country=player_answer, x=country_x, y=country_y)
        correct_guesses.append(player_answer)
        countries_names.remove(player_answer)
        countries_x.remove(country_x)
        countries_y.remove(country_y)


# with open("missed countries.csv", mode="w") as missed_countries:
#     for country in countries_names:
#         missed_countries.write(f"{country}\n")

missed_countries = pandas.DataFrame(countries_names)
missed_countries.to_csv("missed countries.csv")
