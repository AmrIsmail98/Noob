import csv
from _csv import reader, writer

first_file = "data_1.csv"

movies_dict = {}


with open(first_file, "r") as first_csv_file:
    read_csv_file = csv.reader(first_csv_file)
    headers = next(read_csv_file, None)

    for rows in read_csv_file:
        movies_dict[rows[0]] = {headers[i]: rows[i] for i in range(1, len(rows))}

print(movies_dict)

sorted_movies = dict(sorted(movies_dict.items(), key=lambda x: x[1]['Year']))

print(sorted_movies)

with open('year_sorted_movies.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["Title", "Year", "Lead Actor/Actress", "Genres"])

    for key, value in sorted_movies.items():
        row = [key, value['Year'], value['Lead Actor/Actress'], value['Genre']]
        writer.writerow(row)


def old_movies(movies):
    with open("90's_movies.csv", 'w', newline='') as csvfile1:
        writer1 = csv.writer(csvfile1)

        writer1.writerow(["Title", "Year", "Lead Actor/Actress", "Genres"])

        for key1, value1 in movies.items():

            if int(value1['Year']) < 2000:
                row1 = [key1, value1['Year'], value1['Lead Actor/Actress'], value1['Genre']]
                writer1.writerow(row1)

old_movies(sorted_movies)
