import json
from faq_scraper import get_faq_information

def create_faq_dataset(faq_ids_csv, output_jsonl):
    """
    Creates a dataset of FAQs from a list of FAQ IDs.

    This function reads FAQ IDs from a CSV file, fetches the corresponding FAQ data
    using the get_faq_information function, and then writes this data to a JSON Lines (JSONL)
    file for easy consumption in data processing pipelines.

    Args:
    faq_ids_csv (str): Path to the CSV file containing FAQ IDs.
    output_jsonl (str): Path to the output JSONL file where FAQ data will be stored.

    Returns:
    None
    """
    
    # Read the FAQ IDs from a CSV file.
    # Each ID should be separated by a comma in the file.
    with open(faq_ids_csv, 'r') as file:
        faq_ids = file.read().split(',')

    # Process each FAQ ID to fetch and store its corresponding data.
    # The data is written to a JSONL file where each line is a separate JSON object.
    with open(output_jsonl, 'w', encoding='utf-8') as jsonlfile:
        for faq_id in faq_ids:
            # Fetch FAQ data using the provided scraper function.
            data = get_faq_information(faq_id)
            
            if data:
                # Write the FAQ data as a JSON object in the JSONL file.
                # Each object is separated by a newline for readability and processing efficiency.
                json.dump(data, jsonlfile)
                jsonlfile.write('\n')  # Newline to separate JSON objects

    print(f"FAQ dataset has been created and stored in {output_jsonl}.")

if __name__ == "__main__":
    # Define the paths to the input CSV file and the output JSONL file.
    # Adjust these paths as necessary for your project structure.
    faq_ids_csv = 'DB/data/faq_ids.csv'
    output_jsonl = 'DB/data/faqs_dataset.jsonl'

    # Call the function to create the FAQ dataset.
    create_faq_dataset(faq_ids_csv, output_jsonl)
