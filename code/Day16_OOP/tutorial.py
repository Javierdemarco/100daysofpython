# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
pokemon_names = ["Pikachu", "Squirtle", "Charmander"]
types_names = ["Electric", "Water", "Fire"]

table.add_column("Pokemon Name", pokemon_names)
table.add_column("Type", types_names)

table.align = "l"

print(table)
