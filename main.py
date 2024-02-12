import pandas as pd
from fuzzywuzzy import process
import time

df = pd.read_csv('pokemon_data.csv')

pokemon_input = input("Enter the name of a Pokemon you'd like to search: ").strip()

result = list(process.extractOne(pokemon_input, df['Name'], scorer=process.fuzz.ratio))

while True:
    if result[1] >= 80:
        matched_pokemon = result[0].capitalize()
        found = True
        values = []

        for index, row in df.iterrows():
            if row['Name'].capitalize() == matched_pokemon:
                print(df.iloc[index])
                hp = df.iloc[index, 4]
                values.append(hp)
                attack = df.iloc[index, 5]
                values.append(attack)
                special_attack = df.iloc[index, 6]
                values.append(special_attack)
                special_defense = df.iloc[index, 7]
                values.append(special_defense)
                speed = df.iloc[index, 8]
                values.append(speed)
                rating = (sum(values) / 6)
                print("Rating is: " + str(round(rating)) + '%')
        break
    else:
        print(f'"{pokemon_input}" not found. Did you mean "{result[0].capitalize()}"?')
        print('would you like to use suggested pokemon as search value?(yes/no) ')
        time.sleep(0.5)
        check = input('Yes or no: ')[0].lower()
        if check == 'y':
            result[1] = 80
        else:
            break
