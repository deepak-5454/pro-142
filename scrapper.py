import requests
from bs4 import BeautifulSoup
import csv

def scrape_stars_data(pages_to_scrape=5):
    base_url = "https://example-stellar-data-website.com/page/"
    
    # List to store scraped data
    all_stars_data = []

    for page_number in range(1, pages_to_scrape + 1):
        url = f"{base_url}{page_number}"

        # Sending a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract relevant information about stars (modify as needed)
            star_data = []

            # Example: Extracting star names
            star_name_elements = soup.select('.star-name-class')  # Adjust the class selector accordingly
            for star_name_element in star_name_elements:
                star_name = star_name_element.text.strip()
                star_data.append({'Star Name': star_name})

            # Example: Extracting other star information
            # You can add more elements and details to scrape

            # Append the data to the main list
            all_stars_data.extend(star_data)

        else:
            print(f"Failed to retrieve data from {url}. Status Code:", response.status_code)

    return all_stars_data

def save_to_csv(stars_data, output_file='stars_data.csv'):
    # Save the scraped data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = stars_data[0].keys() if stars_data else []
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(stars_data)

if __name__ == "__main__":
    # Set the number of pages to scrape
    pages_to_scrape = 5

    # Scrape star data
    stars_data = scrape_stars_data(pages_to_scrape)

    if stars_data:
        # Save the data to a CSV file
        save_to_csv(stars_data)
        print(f"Scraped data from {pages_to_scrape} pages and saved to 'stars_data.csv'.")
    else:
        print("No data scraped.")
