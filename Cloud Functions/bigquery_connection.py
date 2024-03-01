import functions_framework
from google.cloud import bigquery

@functions_framework.http
def bigquery_connection(request):
    
    client = bigquery.Client()

    # doesn't work to use variable in query - may research more later
    # topic = "Printing"

    # queries for questions where "Printing" is a related_topic
    # use case: user selects topic and we show relevant questions
    query = """
    SELECT question
    FROM mcmaster_library_faq.libans
    WHERE "Printing" IN UNNEST(related_topics) 
    """
    # UNNEST helps access the elements in the array of a cell in related_topics

    # topic: Borrowing
    query1 = """
    SELECT question
    FROM mcmaster_library_faq.libans
    WHERE "Borrowing" IN UNNEST(related_topics)

    """
    query2 = """
    SELECT question, answer
    FROM mcmaster_library_faq.libans
    WHERE answer IS NOT NULL;

    """
    query3 = """
    SELECT answer
    FROM mcmaster_library_faq.libans
    WHERE faq_id = 204885;

    """




    results = client.query(query2)

    qs = []

    # saves each question into an array
    for row in results:
        #print(f'{related_topics:<20} | {count:>3,}')

        # print doesn't work?
        print("here")

        question = row['question']
        answer = row['answer']
        qs.append(question)
        qs.append(answer)

    # returns questions array with all questions with related_topic containing  "Printing"
    return qs

# cmd to run in cloud shell:
# curl -m 70 -X POST https://northamerica-northeast2-macfaqchatbot.cloudfunctions.net/bigquery-connection -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{}'

# related_topics = "Printing"
# Output: ["How do I add money to my PrintSmart account?","How do I change/reset my PrintSmart PIN?","I forgot my student/McMaster ID card, can I still print?","Does the library have 3D printers? Can I use them?","Where can I print and scan? How much does it cost?"]

