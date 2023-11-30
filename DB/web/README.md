
# McMaster Library FAQ Database Generation

This guide outlines the steps to generate a database for McMaster Library's FAQ section using Python scripts.

## Overview

The process involves two main steps:
1. **Extracting FAQ IDs**: Fetching FAQ IDs from the library's sitemap.
2. **Creating FAQ Database**: Generating a JSON Lines (JSONL) file containing FAQ data.

## Prerequisites

Ensure you have Python installed along with the `requests` module. You can install the required module using:

```bash
pip install requests
```

## Step 1: Extracting FAQ IDs

Run the script to extract FAQ IDs from the McMaster Library sitemap.

```bash
python DB/web/extract_faq_ids_from_sitemap.py
```

This script:
- Fetches the XML sitemap from the specified URL.
- Parses the XML to find URLs containing '/faq/'.
- Extracts and stores the FAQ IDs in `DB/data/faq_ids.csv`.

## Step 2: Creating the FAQ Database

Once you have the FAQ IDs, run the following script to create the FAQ database.

```bash
python DB/web/create_faq_dataset.py
```

This script:
- Reads the FAQ IDs from `DB/data/faq_ids.csv`.
- Fetches FAQ information for each ID using a custom scraping function.
- Writes the collected FAQ data into a JSONL file at `DB/data/faqs_dataset.jsonl`.

## Result

After running these scripts, you'll have a JSONL file (`DB/data/faqs_dataset.jsonl`) containing the complete dataset of FAQs from the McMaster Library website, ready for further use or analysis.
