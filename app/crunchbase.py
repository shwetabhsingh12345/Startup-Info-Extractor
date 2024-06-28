import requests

def get_crunchbase_data(startup_name):
    api_key = 'Your API key'
    url = f'https://api.crunchbase.com/v3.1/organizations/{startup_name}?user_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information from the JSON response
        organization = data.get('data', {}).get('properties', {})
        
        return {
            'funding_rounds': organization.get('funding_rounds', 'N/A'),
            'founded_year': organization.get('founded_on_year', 'N/A'),
            'location': organization.get('city_name', 'N/A')
        }
    else:
        return {}

if __name__ == '__main__':
    print(get_crunchbase_data('example-startup'))
