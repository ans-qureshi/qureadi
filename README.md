# Qureadi

## Mendeley Integration with OAuth 2.0

This application allows users to integrate with Mendeley's API using OAuth 2.0 authentication. The app fetches user-specific data, such as their library, and organizes it in a structured format, which can be exported to a spreadsheet for easy review and categorization.

---

## Features
- Authenticate users securely via Mendeley's OAuth 2.0.
- Fetch user-specific data such as document titles, authors, DOIs, and more.
- Organize fetched data into structured categories for research purposes.
- Export the organized data to a spreadsheet for easy tracking and reference.

---

## Prerequisites
1. **Python 3.7 or above**: Ensure Python is installed on your system.
2. **Required Libraries**: Install the following Python libraries:
   ```bash
   pip install requests flask openpyxl
   ```
3. **Mendeley Developer Account**: 
   - Register a Mendeley app at the [Mendeley Developer Portal](https://dev.mendeley.com/).
   - Obtain the following:
     - Client ID
     - Client Secret
     - Redirect URI (e.g., `http://localhost:8000/callback`)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mendeley-integration.git
   cd mendeley-integration
   ```

2. Set up your environment variables:
   Create a `.env` file in the project directory with the following content:
   ```
   CLIENT_ID=your_mendeley_client_id
   CLIENT_SECRET=your_mendeley_client_secret
   REDIRECT_URI=http://localhost:8000/callback
   ```

3. Run the Flask app to handle OAuth redirect URIs:
   ```bash
   python redirect_server.py
   ```

4. Run the main script to start the integration:
   ```bash
   python main.py
   ```

---

## Usage

### Step 1: Authenticate
- The application will redirect you to Mendeley's login page to authenticate and authorize the app.
- Once authenticated, an access token is retrieved and used for subsequent API calls.

### Step 2: Fetch and Organize Data
- The app fetches user library data from Mendeley and organizes it into structured categories.
- The data includes:
  - Title
  - Authors
  - DOI
  - Year
  - Method
  - Results
  - Evaluation Method

### Step 3: Export Data to a Spreadsheet
- Export the organized data to a spreadsheet for easy categorization and reference.
- Each research category can be stored on a separate sheet in the spreadsheet.

---

## Folder Structure
```
mendeley-integration/
│
├── redirect_server.py      # Flask app to handle OAuth redirect URIs
├── main.py                 # Main script for Mendeley integration
├── utils/
│   ├── api_client.py       # Handles Mendeley API requests
│   ├── data_organizer.py   # Organizes fetched data into structured formats
│   └── spreadsheet.py      # Exports organized data to a spreadsheet
├── .env                    # Environment variables
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

---

## Troubleshooting

### Invalid Token Error
If you encounter the error:
```
{'message': 'Could not access resource because: Token is invalid'}
```
- Ensure your access token hasn't expired. Re-authenticate to retrieve a new token.

### Callback URL Issues
If the app cannot connect to the callback URL (`http://localhost:8000/callback`):
- Ensure the Flask app (`redirect_server.py`) is running.
- Verify that your Mendeley app's redirect URI matches `http://localhost:8000/callback`.

---

## Future Enhancements
- Add a refresh token flow for seamless token renewal.
- Support public data access for non-authenticated operations.
- Integrate additional export formats (e.g., CSV, JSON).
- Add a web-based dashboard for managing research categories and viewing data.

---

## Contributing
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- [Mendeley Developer Portal](https://dev.mendeley.com/)
- [OAuth 2.0 Guide](https://oauth.net/2/)



### Customization Notes:
- Replace placeholder URLs, app names, or repository links with your project's specifics.
- Add an example output screenshot (optional) to make it visually appealing. 

