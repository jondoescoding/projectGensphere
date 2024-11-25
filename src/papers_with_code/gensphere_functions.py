# product_hunt_search_functions.py

from datetime import datetime
from bs4 import BeautifulSoup



def read_file_as_string(file_path):

    try:

        with open(file_path, 'r') as file:

            content = file.read()

        return {'domains':content}

    except FileNotFoundError:

        return "Oops! It seems the specified file doesn't exist. Please provide a valid file path."

        

def get_current_date_function():

    return {'current_date':datetime.today().strftime('%Y-%m-%d')}

    

def get_timewindow_function():

    return {'time_window':'past day'}

        

def postprocess_search_results_functions(info):

    result=info.model_dump().get('information_list')

    return {'postprocessed_search_results':result}



def extract_paper_urls(html_content):
    """
    Extracts paper URLs from Papers with Code cards
    
    Args:
        html_content (str): HTML content of the page
        
    Returns:
        dict: Dictionary containing list of extracted URLs
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all paper cards (based on the structure shown)
        paper_cards = soup.find_all('div', class_='row infinite-item item paper-card')
        
        paper_urls = []
        for card in paper_cards:
            # Find the paper link - typically in an <a> tag
            paper_link = card.find('a', href=True)
            if paper_link:
                url = f"https://paperswithcode.com{paper_link['href']}"
                paper_urls.append(url)
        
        return {'paper_urls': paper_urls}
        
    except Exception as e:
        return {'error': f"Error extracting URLs: {str(e)}"}


