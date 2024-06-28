from flask import Blueprint, request, render_template
from .scrape import scrape_website
from .nlp import extract_information
from .crunchbase import get_crunchbase_data

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/submit', methods=['POST'])
def submit():
    url = request.form['url']
    startup_name = request.form['startup_name']
    website_text = scrape_website(url)
    info = extract_information(website_text)
    
    crunchbase_data = get_crunchbase_data(startup_name)

    if isinstance(crunchbase_data, dict):
        info.update(crunchbase_data)
    else:
        print("Unexpected format for Crunchbase data.")
    
    return render_template('result.html', info=info)
