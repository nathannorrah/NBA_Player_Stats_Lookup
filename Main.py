import csv
import sys

filenames = [
    '2021-2022 NBA Player Stats - Regular.csv',
    '2022-2023 NBA Player Stats - Regular.csv',
    '2023-2024 NBA Player Stats - Regular.csv'
]

all_players = {}

encoding_types = ['latin-1', 'utf-16', 'iso-8859-1']

for filename in filenames:
  for encoding_type in encoding_types:
    try:
      with open(filename, 'r', encoding=encoding_type) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
          player_name = row[1]
          team = row[4]

          if player_name not in all_players:
            all_players[player_name] = {
                'PPG': [],
                'RPG': [],
                'APG': [],
                'BPG': [],
                'SPG': [],
                'FG%': [],
                'Teams': {}
            }

          if team not in all_players[player_name]['Teams']:
            all_players[player_name]['Teams'][team] = {
                'PPG': [],
                'RPG': [],
                'APG': [],
                'BPG': [],
                'SPG': [],
                'FG%': [],
                'Year': filename[:9]  # Extracting the year from the filename
            }

          all_players[player_name]['PPG'].append(row[29])
          all_players[player_name]['RPG'].append(row[23])
          all_players[player_name]['APG'].append(row[24])
          all_players[player_name]['BPG'].append(row[26])
          all_players[player_name]['SPG'].append(row[25])
          all_players[player_name]['FG%'].append(row[10])
          all_players[player_name]['Teams'][team]['PPG'].append(row[29])
          all_players[player_name]['Teams'][team]['RPG'].append(row[23])
          all_players[player_name]['Teams'][team]['APG'].append(row[24])
          all_players[player_name]['Teams'][team]['BPG'].append(row[26])
          all_players[player_name]['Teams'][team]['SPG'].append(row[25])
          all_players[player_name]['Teams'][team]['FG%'].append(row[10])

      break
    except UnicodeDecodeError:
      print(f"Error decoding {filename} with {encoding_type} encoding.")

name = input("Enter the player whose stats you would like to view: ")

if name.lower() in (player.lower() for player in all_players.keys()):
  print("\nPlayer found!\n")
  for player_team, stats in all_players[name]['Teams'].items():
    print("Year:", stats['Year'])
    print("Team:", player_team)
    print("Stats for", name)
    print("PPG:", ', '.join(stats['PPG']))
    print("RPG:", ', '.join(stats['RPG']))
    print("APG:", ', '.join(stats['APG']))
    print("BPG:", ', '.join(stats['BPG']))
    print("SPG:", ', '.join(stats['SPG']))
    print("FG%:", ', '.join(stats['FG%']))
    print()  # Printing a newline for spacing
else:
  print("\nPlayer not found.")

sys.exit()
