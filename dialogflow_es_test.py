import json
from flask import jsonify
from google.cloud import bigquery

def dialogflow_es_test(request):
    # Get the JSON request from Dialogflow
    request_json = request.get_json()

    # Extract parameters from the request
    intent_name = request_json["queryResult"]["intent"]["displayName"]
    parameters = request_json["queryResult"]["parameters"]

    # Create a SQL query for big query
    sql_query = f"SELECT * FROM mcmaster_library_faq.libans LIMIT 1"

    # call the Big query function using your created SQL query
    client = bigquery.Client()
    result = client.query(sql_query)

    extracted_data = []
    for row in result:
            question = row.get("question", "")
            answer = row.get("answer", "")

            # Append the extracted data to the list
            extracted_data.append(answer)

    # Prepare the response in Dialogflow ES webhook format
    response = {
        "fulfillmentText": ', '.join(extracted_data),
        "payload": {},  # You can include additional data in the payload if needed
    }

    # Return the response as JSON
    return jsonify(response)



