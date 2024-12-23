import requests
import webbrowser
from urllib.parse import urlparse, parse_qs

# Mendeley credentials
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "http://localhost:8000/callback"
scope = "all"  # Specify the required scope(s), 'all' for full access

# Step 1: Redirect the user to Mendeley's authorization URL
def get_authorization_code():
    auth_url = "https://api.mendeley.com/oauth/authorize"
    authorization_url = f"{auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code"
    print(f"Please go to the following URL to authorize the application: {authorization_url}")
    webbrowser.open(authorization_url)

# Step 2: Get the authorization code after the user grants access
def exchange_code_for_token(authorization_code):
    token_url = "https://api.mendeley.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    
    response = requests.post(token_url, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        refresh_token = token_data['refresh_token']
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
        return access_token, refresh_token
    else:
        print(f"Failed to get access token: {response.json()}")
        return None, None

# Step 3: Use the access token to make an API request
def fetch_user_documents(access_token):
    library_url = "https://api.mendeley.com/catalog/users/me/documents"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(library_url, headers=headers)
    
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to fetch documents: {response.json()}")

# Step 4: Refresh the access token using the refresh token when expired
def refresh_access_token(refresh_token):
    token_url = "https://api.mendeley.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    
    response = requests.post(token_url, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        new_access_token = token_data['access_token']
        print(f"New Access Token: {new_access_token}")
        return new_access_token
    else:
        print(f"Failed to refresh token: {response.json()}")
        return None

# Main logic to handle the entire flow
def main():
    # Step 1: Get the authorization code by redirecting the user to Mendeley's authorization URL
    get_authorization_code()

    # Step 2: Get the authorization code after user authentication
    redirect_response = input("Paste the full redirect URL here: ")
    parsed_url = urlparse(redirect_response)
    authorization_code = parse_qs(parsed_url.query).get("code")[0]

    # Exchange the authorization code for an access token
    access_token, refresh_token = exchange_code_for_token(authorization_code)
    
    if access_token and refresh_token:
        # Step 3: Fetch user documents using the access token
        fetch_user_documents(access_token)
        
        # Example of handling token expiry (assuming access token expires after a certain period)
        try:
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get("https://api.mendeley.com/catalog/users/me/documents", headers=headers)
            
            # If access token expired, refresh it
            if response.status_code == 401:  # Unauthorized (invalid token)
                print("Access token expired. Refreshing token...")
                access_token = refresh_access_token(refresh_token)
                
                # After refreshing the token, retry fetching documents
                if access_token:
                    fetch_user_documents(access_token)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
