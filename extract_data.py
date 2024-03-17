import csv
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/teams"

querystring = {"formatType":"odi"}

headers = {
	"X-RapidAPI-Key": "2f3548419emsh40359975e6c6c70p195ad0jsnda1b4fc10cd1",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

if response.status_code == 200:
    data = response.json().get('rank', [])  # Extracting the 'rank' data
    csv_filename = 'teams_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'rating']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)