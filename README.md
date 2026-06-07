# CRUD Flask App with ML

A small Flask-based CRUD web app with an example machine learning model.

## Project Structure

- `app.py` - Flask application entry point
- `ml_model.py` - Example ML model utilities
- `DB.json` - Simple JSON "database" used by the app
- `templates/` - HTML templates (`index.html`, `add.html`, `edit.html`)
- `static/` - Static files (`style.css`)

## Requirements

- Python 3.8+
- Flask

Install dependencies (recommended inside a virtual environment):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install Flask
```

## Run

Start the app:

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Notes

- The app stores data in `DB.json`. Back it up before making destructive changes.
- `ml_model.py` contains example model logic used by the app; adapt as needed.

## Contributing

Make changes, commit, and push to your fork or this repository:

```bash
git add README.md
git commit -m "Add README"
git push
```

## License

No license specified.
