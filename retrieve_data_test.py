from google.cloud import bigquery

def retrieve_data(request):
    try:
        # Parse the request JSON to get the related_topics value
        # request_data = request.get_json()
        related_topics = "Printing"  # request_data.get('related_topics')

        # Check if related_topics is provided
        if not related_topics:
            return {'error': 'Please provide the related_topics parameter.'}, 400

        # Create a BigQuery client
        client = bigquery.Client()

        # Construct the SQL query
        query = f"""
            SELECT faq_id, question
            FROM mcmaster_library_faq.libans
            WHERE 'Printing' IN UNNEST(related_topics)
        """


        # Run the query
        query_job = client.query(query)
        rows = query_job.result()

        # Process rows or send them as a response
        result = [{'faq_id': row['faq_id'], 'question': row['question']} for row in rows]
        if not result:
            return {'fulfillmentText': 'No data found for the provided related_topics.'}, 404

        # Create a list of messages for Dialogflow
        fulfillment_messages = [
            {
                'text': {
                    'text': [row['question']]
                },
                'platform': 'PLATFORM_UNSPECIFIED'
            } for row in result
        ]

        dialogflow_response = {'fulfillmentMessages': fulfillment_messages}

        return dialogflow_response, 200

    except Exception as e:
        print(f'Error executing BigQuery: {e}')
        return {'fulfillmentText': 'Internal Server Error'}, 500