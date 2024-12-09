# import requests
# from bs4 import BeautifulSoup
#
#
# def scrape_terms(url: str) -> str:
#     """Scrapes terms and conditions text from a webpage."""
#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             raise Exception(f"HTTP Error: {response.status_code}")
#         soup = BeautifulSoup(response.text, "html.parser")
#         terms = " ".join([p.text for p in soup.find_all("p")])
#         print("Scraper Agent: Successfully fetched terms.")
#         return terms
#     except Exception as e:
#         print(f"Scraper Error: {e}")
#         return None
#


# from langchain_core.tools import Tool
# from bs4 import BeautifulSoup
# import requests
#
# def scrape_terms(url: str) -> str:
#     """Scrapes terms and conditions from a webpage."""
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise Exception(f"HTTP Error: {response.status_code}")
#     soup = BeautifulSoup(response.text, "html.parser")
#     terms = " ".join([p.text for p in soup.find_all("p")])
#     return terms
#
# scraper_tool = Tool(
#     name="Scrape Terms",
#     func=scrape_terms,
#     description="Scrape terms and conditions from a URL.",
# )


# from langchain_core.tools import Tool
# from bs4 import BeautifulSoup
# import requests
#
# def scrape_terms(url: str) -> str:
#     """Scrapes terms and conditions from a webpage."""
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise Exception(f"HTTP Error: {response.status_code}")
#     soup = BeautifulSoup(response.text, "html.parser")
#     terms = " ".join([p.text for p in soup.find_all("p")])
#
#     return terms
#
# scraper_tool = Tool(
#     name="Scrape Terms",
#     func=scrape_terms,
#     description="Scrape terms and conditions from a URL.",
# )
#
# from langchain_core.tools import Tool
# from bs4 import BeautifulSoup
# import requests
# import logging
#
# # Setup logging
# logging.basicConfig(level=logging.INFO)
#
#
# def scrape_terms(url: str) -> str:
#     """Scrapes terms and conditions from a webpage."""
#     if not url:
#         logging.error("No URL provided.")
#         return "Error: No URL provided."
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#
#     try:
#         response = requests.get(url, headers=headers, timeout=10)
#         if response.status_code != 200:
#             logging.error(f"HTTP Error: {response.status_code}")
#             return f"Error: HTTP Error {response.status_code}"
#
#         soup = BeautifulSoup(response.text, "html.parser")
#         terms = " ".join([p.text for p in soup.find_all("p")])
#
#         logging.info(f"Successfully scraped terms from {url}.")
#         return terms
#
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Request error: {e}")
#         return f"Error: {str(e)}"
#     except Exception as e:
#         logging.error(f"Error parsing the page: {e}")
#         return f"Error: {str(e)}"
#
#
# scraper_tool = Tool(
#     name="Scrape Terms",
#     func=scrape_terms,
#     description="Scrape terms and conditions from a URL.",
# )


from langchain_core.tools import Tool
from bs4 import BeautifulSoup
import requests
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def scrape_terms(url: str) -> str:
    """Scrapes terms and conditions from a webpage and limits the content to 2000 tokens."""
    if not url:
        logging.error("No URL provided.")
        return "Error: No URL provided."

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            logging.error(f"HTTP Error: {response.status_code}")
            return f"Error: HTTP Error {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        # Extract all text from <p> tags
        terms = " ".join([p.text for p in soup.find_all("p")])

        # Tokenize the terms (splitting by whitespace)
        tokens = terms.split()

        # Limit to a maximum of 2000 tokens
        tokens = tokens[:2000]

        # Get the first 500 tokens
        first_part = " ".join(tokens[:500])

        # Get the middle 1000 tokens (from position 500 to 1500)
        middle_part = " ".join(tokens[500:1500])

        # Get the last 500 tokens from the 3/4th position
        three_quarter_start = len(tokens) * 3 // 4  # Starting position for the 3/4 part
        last_part = " ".join(tokens[three_quarter_start:three_quarter_start + 500])

        # Combine all parts
        limited_terms = f"First 500 tokens: {first_part}\n\nMiddle 1000 tokens: {middle_part}\n\nLast 500 tokens (from 3/4): {last_part}"

        logging.info(f"Successfully scraped and processed terms from {url}.")
        return limited_terms

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return f"Error: {str(e)}"
    except Exception as e:
        logging.error(f"Error parsing the page: {e}")
        return f"Error: {str(e)}"

scraper_tool = Tool(
    name="Scrape Terms",
    func=scrape_terms,
    description="Scrape terms and conditions from a URL, limiting to 2000 tokens (with three sections).",
)
