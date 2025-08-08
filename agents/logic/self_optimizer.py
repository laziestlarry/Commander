class SelfOptimizer:
    def __init__(self, agent):
        self.agent = agent

    def optimize(self):
        score = self.agent.evaluate_performance()
        if score < 0.7:
            self.agent.retrain("latest_successful_prompts")
        else:
            self.agent.scale_tasks()