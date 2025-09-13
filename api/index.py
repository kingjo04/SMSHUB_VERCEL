# Vercel WSGI entry for Flask
# Docs: https://vercel.com/docs/functions/runtimes/python

# Import the Flask app object from app.py at the project root.
# Vercel detects the `app` variable and runs it as a WSGI app.
from app import app  # noqa: F401
