class CreatifyAdBuyerClient:
    def optimize_budget(self, current_roi: float, daily_budget: float) -> dict:
        status = "increase" if current_roi > 2.5 else "decrease" if current_roi < 1.5 else "hold"
        new_budget = daily_budget * 1.25 if status == "increase" else daily_budget * 0.8 if status == "decrease" else daily_budget
        return {"recommended_budget": round(new_budget, 2), "status": status}