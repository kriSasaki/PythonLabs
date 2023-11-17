import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_tiobe_data():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the desired class
        table = soup.find('table', class_='table table-striped table-top20')

        if table:
            data = []
            # Extract data from table rows
            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')
                rank = columns[0].get_text(strip=True)
                language = columns[1].get_text(strip=True)
                change = columns[2].get_text(strip=True)
                data.append((rank, language, change))
            
            return data
        else:
            print("Table not found on the TIOBE page.")
            return None
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def plot_histogram(data):
    if not data:
        print("No data to plot.")
        return

    languages = [entry[1] for entry in data]
    ranks = [int(entry[0]) for entry in data]

    plt.barh(languages, ranks, color='skyblue')
    plt.xlabel('Популярность')
    plt.title('Гистограмма популярности языков программирования (TIOBE)')
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    tiobe_data = get_tiobe_data()

    if tiobe_data:
        print("Data from TIOBE:", tiobe_data)
        plot_histogram(tiobe_data)
    else:
        print("Failed to retrieve TIOBE data.")
