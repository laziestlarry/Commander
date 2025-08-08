class DecisionTreeAI:
    def __init__(self):
        self.state = {}

    def evaluate(self, agent_data):
        if agent_data.get("missions_completed", 0) < 5:
            return "boost_training"
        elif agent_data.get("success_rate", 0) < 0.6:
            return "retrain_with_examples"
        else:
            return "launch_sales_sequence"