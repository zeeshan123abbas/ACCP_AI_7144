# rate_calculator.py
# A simple helper to find your minimum hourly rate and a project price.

# Step 1: your numbers (change these)
monthly_target_usd = 400      # money you want to keep each month
monthly_expenses_usd = 60     # internet, electricity, software, hosting
billable_hours = 80           # hours of paid client work per month
platform_fee_percent = 20     # platform service fee (check current rate)

# Step 2: money needed before the platform fee is taken
needed_after_fee = monthly_target_usd + monthly_expenses_usd
needed_before_fee = needed_after_fee / (1 - platform_fee_percent / 100)

# Step 3: minimum hourly rate
hourly_rate = needed_before_fee / billable_hours
print("Minimum hourly rate: $", round(hourly_rate, 2))

# Step 4: price one project
estimated_hours = 15          # e.g. a 5-page WordPress website
buffer = 1.2                  # 20% extra for revisions and calls
project_price = estimated_hours * hourly_rate * buffer
print("Suggested project price: $", round(project_price, 2))
