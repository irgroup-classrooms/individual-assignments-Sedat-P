import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Listbox
from PIL import Image, ImageTk
from io import BytesIO

# Step 1: Webscraping
def scrape_pokemon_data():
    url = "https://pokemondb.net/pokedex/all"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'pokedex'})

    headers = [th.text for th in table.find('thead').find_all('th')]
    rows = []
    for tr in table.find('tbody').find_all('tr'):
        cols = [td.text.strip() for td in tr.find_all('td')]
        sprite_url = tr.find('td').find('img')['src']  # Sprite image
        cols.append(sprite_url)
        rows.append(cols)

    headers.append("Sprite")
    df = pd.DataFrame(rows, columns=headers)
    return df

pokemon_df = scrape_pokemon_data()
print("Columns in the DataFrame:", pokemon_df.columns)

# Ensure correct column names
if 'Type 1' not in pokemon_df.columns:
    pokemon_df.rename(columns={'Type': 'Type 1'}, inplace=True)

# Ensure numeric columns are properly converted
numeric_columns = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
for col in numeric_columns:
    if col in pokemon_df.columns:
        pokemon_df[col] = pd.to_numeric(pokemon_df[col], errors='coerce')

pokemon_df.to_csv("pokemon_data.csv", index=False)
print("Data scraped and saved to pokemon_data.csv")

# Step 2: Exploratory Data Analysis
def strongest_pokemon(df):
    strongest = df.sort_values(by='Total', ascending=False).groupby('Type 1').first()
    print("Strongest Pokemon by Type:\n", strongest[['Name', 'Total']])

def best_attackers(df):
    best = df.sort_values(by='Attack', ascending=False).head(10)
    print("Best Attackers:\n", best[['Name', 'Attack']])

def average_stats(df):
    averages = df.groupby('Type 1').mean(numeric_only=True)
    print("Average Stats by Type:\n", averages[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])

strongest_pokemon(pokemon_df)
best_attackers(pokemon_df)
average_stats(pokemon_df)

# Step 3: BONUS - GUI Application
def show_pokemon_data():
    def display_sprite(event):
        selected = listbox.get(listbox.curselection())
        sprite_url = pokemon_df[pokemon_df['Name'] == selected]['Sprite'].values[0]
        response = requests.get(sprite_url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        sprite_label.configure(image=img)
        sprite_label.image = img

    root = Tk()
    root.title("Pokemon Viewer")

    Label(root, text="Select a Pokemon:").pack()

    listbox = Listbox(root)
    for name in pokemon_df['Name']:
        listbox.insert('end', name)
    listbox.pack()

    sprite_label = Label(root)
    sprite_label.pack()

    listbox.bind("<<ListboxSelect>>", display_sprite)

    Button(root, text="Exit", command=root.quit).pack()

    root.mainloop()

# Uncomment below to launch GUI application
# show_pokemon_data()
