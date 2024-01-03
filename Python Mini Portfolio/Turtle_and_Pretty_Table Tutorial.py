from prettytable import PrettyTable

table = PrettyTable()
# columns are Adding Data Vertically:
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Types", ["Electric", "Water", "Fire"])

table.align = 'l'

print(table)
