"""Print a text burndown chart and today's status from sprint data.
Run: python burndown.py
"""
total_points = 40
sprint_days = 10
remaining = [40, 37, 35, 30, 28, 22, 18]          # recorded at end of each day so far

ideal_per_day = total_points / sprint_days
print("Day | Ideal | Actual | Chart")
for day, actual in enumerate(remaining, start=1):
    ideal = total_points - ideal_per_day * day
    bar = "#" * int(actual)
    flag = "  <-- behind" if actual > ideal else ""
    print(f"{day:>3} | {ideal:5.1f} | {actual:6} | {bar}{flag}")

days_used = len(remaining)
burned = total_points - remaining[-1]
velocity_per_day = burned / days_used
days_needed = remaining[-1] / velocity_per_day
print(f"\nAverage burn: {velocity_per_day:.1f} pts/day")
print(f"Forecast: {days_needed:.1f} more days needed, {sprint_days - days_used} days left")
