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
    # Consider adding error handling for network issues or unexpected response formats.
    response = requests.get(sitemap_url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the XML content from the response.
        # The XML namespace is defined because the sitemap follows a specific schema.
        root = ET.fromstring(response.content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        faq_ids = []

        # Iterate through each URL found in the sitemap.
        # The namespace ('ns') is used to match the elements in the sitemap's schema.
        for url in root.findall('ns:url', namespace):
            loc = url.find('ns:loc', namespace)
            # Check if the URL element exists and specifically contains '/faq/' in its text.
            # This condition identifies URLs that are relevant to FAQs.
            if loc is not None and '/faq/' in loc.text:
                # Extract the FAQ ID from the URL's last segment and add it to the list.
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
    # Adjust these paths as necessary for your specific deployment or usage.
    sitemap_url = "https://libanswers.mcmaster.ca/sitemap.xml"
    output_file = "DB/data/faq_ids.csv"

    # Call the function to fetch and store FAQ IDs.
    fetch_and_store_faq_ids(sitemap_url, output_file)
