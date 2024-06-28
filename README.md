# Startup Info Extractor

Startup Info Extractor is a web application that extracts and displays key information about startups. It scrapes the startup's website for relevant information and fetches additional data from the Crunchbase API.

## Features

- Scrapes startup websites to extract key information such as description, industry, customers, and geography.
- Fetches additional data from the Crunchbase API including funding rounds, founded year, and location.
- Displays the extracted information in a user-friendly format.

## Requirements

- Python 3.10 or higher
- Flask
- Requests
- Transformers
- BeautifulSoup4

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/startup-info-extractor.git
   cd startup-info-extractor
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Obtain a Crunchbase API key from the [Crunchbase Developer Portal](https://data.crunchbase.com/docs/using-the-api).
2. Replace the `api_key` variable in the `crunchbase.py` file with your Crunchbase API key.

## Usage

1. Run the application:

   ```bash
   python run.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Fill in the form with the startup's website URL and name, then click the "Submit" button.

4. View the extracted and fetched information displayed on the results page.

## Project Structure

```
startup-info-extractor/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── scrape.py
│   ├── nlp.py
│   └── crunchbase.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── results.html
├── requirements.txt
├── run.py
└── README.md
```

- `app/`: Contains the main application files.
  - `__init__.py`: Initializes the Flask app.
  - `routes.py`: Defines the routes and views for the Flask app.
  - `scrape.py`: Contains the web scraping logic.
  - `nlp.py`: Contains the natural language processing logic.
  - `crunchbase.py`: Contains the logic to fetch data from Crunchbase API.
- `static/`: Contains static files such as CSS.
- `templates/`: Contains HTML templates for the web app.
- `requirements.txt`: Lists the required Python packages.
- `run.py`: The entry point for the Flask app.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework used.
- [Requests](https://requests.readthedocs.io/) - Library for making HTTP requests.
- [Transformers](https://huggingface.co/transformers/) - Library for natural language processing.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Library for web scraping.
