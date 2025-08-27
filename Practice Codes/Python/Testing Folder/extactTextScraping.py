import requests
from bs4 import BeautifulSoup
from docx import Document

def scrape_and_save(url):
    """
    Extracts text from a given URL and saves it to a .txt and .docx file.
    """
    try:
        # 1. Fetch the webpage content
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status() 
        print(f"Successfully fetched the URL: {url}")

        # 2. Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # 3. Extract all the text from the webpage
        # The .get_text() method returns all the text in the document.
        # separator=' ' joins separate text blocks with a space.
        # strip=True removes leading/trailing whitespace from each text block.
        page_text = soup.get_text(separator=' ', strip=True)

        # 4. Save the text to a .txt file
        with open('scraped_content.txt', 'w', encoding='utf-8') as f:
            f.write(page_text)
        print("Text saved to scraped_content.txt")

        # 5. Save the text to a .docx file
        doc = Document()
        doc.add_paragraph(page_text)
        doc.save('scraped_content.docx')
        print("Text saved to scraped_content.docx")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Replace this with the URL you want to scrape
    target_url = "https://rootstack.com/en/blog/java-clear-screen" 
    scrape_and_save(target_url)