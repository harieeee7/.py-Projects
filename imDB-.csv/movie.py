import pandas as pd

# Define path where your CSV file is present
csv_path = r'C:\Users\harih\Downloads\Py_Pros\IMDB-Movie-Data.csv'

# Load data from CSV file
try:
    movie_data = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Error: '{csv_path}' file not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: '{csv_path}' file is empty.")
    exit(1)
except pd.errors.ParserError as e:
    print(f"Error parsing CSV: {e}")
    exit(1)

# User inputs the movie title
user_input = input("Enter the movie title: ").strip().lower()

# Flag to check if the movie is found
found = False

# Iterating through each row in the CSV to find the requested movie
for index, row in movie_data.iterrows():
    title = row.get('Title', '').strip().lower()  # Adjust 'Title' based on your column name

    if user_input in title:
        found = True
        rank = row.get('Rank', 'N/A')
        genre = row.get('Genre', 'N/A')
        description = row.get('Description', 'N/A')
        director = row.get('Director', 'N/A')
        actors = row.get('Actors', 'N/A')
        year = row.get('Year', 'N/A')
        runtime = row.get('Runtime (Minutes)', 'N/A')
        rating = row.get('Rating', 'N/A')
        votes = row.get('Votes', 'N/A')
        revenue = row.get('Revenue (Millions)', 'N/A')
        metascore = row.get('Metascore', 'N/A')

        print(f"\nMovie found:\n"
              f"Rank: {rank}\n"
              f"Title: {title.title()}\n"
              f"Genre: {genre}\n"
              f"Description: {description}\n"
              f"Director: {director}\n"
              f"Actors: {actors}\n"
              f"Year: {year}\n"
              f"Runtime: {runtime} minutes\n"
              f"Rating: {rating}\n"
              f"Votes: {votes}\n"
              f"Revenue: ${revenue} million\n"
              f"Metascore: {metascore}")
        break

if not found:
    print(f"Movie '{user_input}' not found in the CSV file.")
