"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
is_valid = True
#Get age
user_age = int(float(input("Please enter your age : ")))
#Calculate max
max_rate = 220 - user_age
#Calculate max range
max_range = int(max_rate * 0.85)
#Calculate min range
min_range = int(max_rate * 0.65)
#Display max and min range
print(f"When you exercise to strengthen your heart,\n you should keep your heart rate between {min_range} and {max_range} beats per minute.")