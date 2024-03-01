import functions_framework

@functions_framework.http
def webhook_test(request):

    # https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookRequest req info
    req = request.get_json()

    tag = req["fulfillmentInfo"]["tag"]

    if tag == "Default Welcome Intent":
        text = "Hello from a GCF Webhook"
    elif tag == "get-name":
        text = "My name is Flowhook"
    else:
        text = f"There are no fulfillment responses defined for {tag} tag"


    # this is where relevant info will go to big query


    # this is where you build the response to send back to dialogflow
    # https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookResponse res info
    res = {"fulfillment_response": {"messages": [{"text": {"text": [text]}}]}}

    # Returns json
    return res
