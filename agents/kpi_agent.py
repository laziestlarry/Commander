class KPIAgent:
    def track(self, metric, value):
        print(f"[KPI] {metric}: {value}")
        # Save to DB, trigger alerts, or update dashboard here
