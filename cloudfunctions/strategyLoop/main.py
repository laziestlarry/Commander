import functions_framework
from agents.trainer import train_agents_with_playbook
from scenarios.weekly_scenarios import get_weekly_missions
from services.telegram_notifier import send_telegram_report

@functions_framework.http
def strategyLoop(request):
    try:
        missions = get_weekly_missions()
        results = train_agents_with_playbook(missions)
        send_telegram_report("✅ Weekly strategy training complete. Agents trained.")
        return "Strategy loop completed", 200
    except Exception as e:
        send_telegram_report(f"❌ Strategy loop failed: {str(e)}")
        return f"Error: {str(e)}", 500