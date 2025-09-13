# Deploying SMSHUB to Vercel (Flask + Supabase)

This folder is prepped to run on **Vercel Functions (Python)** using Flask (WSGI).

## What we changed
- Added **`api/index.py`** (WSGI entry) so Vercel can run your Flask `app`.
- Added **`vercel.json`** to route all paths to the WSGI function and set the Python runtime.
- Patched **`app.py`** to read **`SMSHUB_API_KEY`** from environment (fallback to `config.ini` for local dev).
- Left `requirements.txt` as-is (Gunicorn is not used on Vercel but harmless).

> ⚠️ Do **not** commit secrets. Prefer Vercel Environment Variables.

## One‑time setup (GitHub → Vercel)
1. Create a **private** GitHub repo and push this folder.
2. On **Vercel Dashboard** → *Add New Project* → import the repo.
3. Add Environment Variables (for *Production*, *Preview*, and *Development*):
   - `SMSHUB_API_KEY` = your API key
   - `SUPABASE_URL`   = your project URL
   - `SUPABASE_KEY`   = your anon/service key
4. Click **Deploy**.

## Local development
Option A (Flask dev server):  
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export SMSHUB_API_KEY=... SUPABASE_URL=... SUPABASE_KEY=...
python app.py
```
Open http://127.0.0.1:5000

Option B (Vercel CLI):  
```bash
npm i -g vercel
vercel dev
```
> Note: Vercel CLI has limited Python emulation locally. If you hit issues, use Option A.

## Notes
- Filesystem on Vercel Functions is **read‑only**; only `/tmp` is writable and ephemeral. Use Supabase for persistence.
- Default Python on Vercel is **3.12** (can be set via Pipfile if you need a specific version).
- You can change region in `vercel.json` (currently `sin1`).

## Troubleshooting
- 404 on routes → ensure `vercel.json` exists and rewrites to `/api/index`.
- Import errors → the working directory is the project root, so `from app import app` should work.
- Timeouts → keep requests quick; Hobby has lower max duration than Pro.
