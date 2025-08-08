# AutonomaX Commander App

## Flask Dashboard

- `dashboard_flask.py`: Flask app for unified dashboard, archive, and action triggering.
- `templates/`: HTML templates for dashboard and archive views.
- `archive/`: Stores critical resources, completions, and valuables for project/process archiving.

## Usage

1. Install Flask if not already installed:
   ```bash
   pip install flask
   ```
2. Run the dashboard:
   ```bash
   python app/dashboard_flask.py
   ```
3. Open your browser at http://127.0.0.1:5000/

## Next Steps
- Integrate persistent storage (e.g., SQLite, JSON, or cloud DB)
- Expand dashboard modules for CRM, team, market analysis, calendar, and reporting
- Connect with orchestrator and automation modules
