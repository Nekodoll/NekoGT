import threading
import requests
from bs4 import BeautifulSoup
import time
import os


class TableScraper:
    def __init__(self):
        # Prompt the user for the headers, cookie, url, and table_url values
        self.headers = input("Enter the headers as a dictionary: ")
        self.cookie = input("Enter the cookie string: ")
        self.url = input("Enter the URL of the website: ")
        self.table_url = input("Enter the URL of the table: ")
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": self.headers,
            "Cookie": self.cookie,
        }

        # Initialize timer
        self.start_time = time.perf_counter()
        self.refresh_rate = 60  # Refresh rate in seconds

    def run(self):
        while True:
            # Calculate elapsed time and sleep time
            elapsed_time = time.perf_counter() - self.start_time
            sleep_time = self.refresh_rate - elapsed_time
            if sleep_time < 0:
                sleep_time = 0

            # Send a POST request to the URL
            try:
                response = requests.post(self.url, headers=self.headers)
            except Exception as e:
                print(f"An error occurred while making the POST request: {e}")
                continue

            # Print the title of the website in blue
            try:
                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string
                os.system("cls" if os.name == "nt" else "clear")
                print("\033[33m" + title + " Success Claim\033[0m")
            except Exception as e:
                print(f"An error occurred while parsing the HTML content: {e}")
                continue

            # Send a GET request to the table URL
            try:
                response = requests.get(self.table_url, headers=self.headers)
            except Exception as e:
                print(f"An error occurred while making the GET request: {e}")
                continue

            # Parse the HTML content and find the table element
            try:
                soup = BeautifulSoup(response.text, "html.parser")
                table = soup.find("table")
            except Exception as e:
                print(f"An error occurred while parsing the HTML content: {e}")
                continue

            # Print the table text without the header row
            for row in table.find_all("tr")[1:]:
                cells = row.find_all("td")
                row_text = " ".join(cell.text for cell in cells)
                print("\033[92m" + row_text + "\033[0m")

            # Refresh the timer
            self.start_time = time.perf_counter()

            # Sleep for the remaining time
            time.sleep(sleep_time)

        def main():
            # Create a separate thread for the scraper
            scraper_thread = threading.Thread(target=TableScraper().run)

            # Set the thread as a daemon thread
            scraper_thread.daemon = True

            # Start the thread
            scraper_thread.start()

            # Wait for keyboard interrupt
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
