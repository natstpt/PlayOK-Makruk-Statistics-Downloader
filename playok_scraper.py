import requests
from bs4 import BeautifulSoup
import re
import os

# Get user input for the ID
user_id = input("Please enter the ID (e.g., cpm1399g): ")

# Initialize the extracted values list, page number, and download counter
extracted_values = []
page_number = 1
downloaded_files_count = 0

# Create a data directory if it doesn't exist
if not os.path.exists("txtdata"):
    os.makedirs("txtdata")

while True:
    # Concatenate the user input to the URL and include the incremented page query parameter
    url = f'https://www.playok.com/en/stat.phtml?u={user_id}&g=mk&sk=2&page={page_number}'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        target_elements = soup.find_all(
            'a', {'target': '_blank', 'href': lambda x: x and x.startswith('/p/?g=mk')})

        if not target_elements:
            print("Searched for the game until the last page")
            break

        for element in target_elements:
            href_value = element.get('href')
            match = re.search(r"mk(\d+)\.txt", href_value)
            if match:
                extracted_text = match.group(1)
                extracted_values.append(extracted_text)
                url_txt = f'https://www.playok.com/p/?g=mk{extracted_text}.txt'
                print(f"Downloaded files url: {url_txt}")

                # Download the .txt file
                txt_response = requests.get(url_txt)

                if txt_response.status_code == 200:
                    # Save the .txt file in the data directory
                    with open(f"txtdata/mk{extracted_text}.txt", "w") as file:
                        file.write(txt_response.text)

                    # Increment the download counter
                    downloaded_files_count += 1
                else:
                    print(
                        f"Failed to download the .txt file. Status code: {txt_response.status_code}")

        # Increment the page number for the next iteration
        page_number += 1
    else:
        print(
            f"Failed to fetch the webpage. Status code: {response.status_code}")
        break

print(f"Total page number: {page_number}")
print(f"Downloaded files: {downloaded_files_count}")
