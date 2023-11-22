import requests
import xml.etree.ElementTree as ET

def fetch_and_store_faq_ids(sitemap_url, output_file):
    """
    Fetches FAQ IDs from a sitemap URL and stores them in a specified file.

    This function sends a request to the provided sitemap URL, parses the XML content
    to extract FAQ page URLs, retrieves FAQ IDs from these URLs, and then writes these IDs
    to a specified output file, separated by commas.

    Args:
    sitemap_url (str): URL of the sitemap containing links to FAQ pages.
    output_file (str): Path to the file where extracted FAQ IDs will be stored.

    Returns:
    None
    """
    
    # Send a GET request to the sitemap URL.
    response = requests.get(sitemap_url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the XML content from the response.
        root = ET.fromstring(response.content)
        # Define the namespace used in the sitemap XML.
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        faq_ids = []

        # Iterate through each URL found in the sitemap.
        for url in root.findall('ns:url', namespace):
            loc = url.find('ns:loc', namespace)
            # Check if the URL element exists and contains '/faq/' in its text.
            if loc is not None and '/faq/' in loc.text:
                # Extract the FAQ ID from the URL and add it to the list.
                faq_id = loc.text.strip().rsplit('/', 1)[-1]
                faq_ids.append(faq_id)

        # Write the collected FAQ IDs to the specified output file.
        with open(output_file, 'w') as f:
            f.write(','.join(faq_ids))
        print(f"FAQ IDs have been stored in {output_file}")
    else:
        # Print an error message if the request was unsuccessful.
        print(f"Failed to retrieve the sitemap, status code: {response.status_code}")

if __name__ == "__main__":
    # Define the URL of the sitemap and the path to the output file.
    sitemap_url = "https://libanswers.mcmaster.ca/sitemap.xml"
    output_file = "DB/data/faq_ids.csv"

    # Call the function to fetch and store FAQ IDs.
    fetch_and_store_faq_ids(sitemap_url, output_file)
