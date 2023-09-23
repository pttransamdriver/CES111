age = int(input("What is your age?: "))
heart_rate = 220 - age
high = heart_rate * .85
low = heart_rate * .65
print(f"For a healty human your heart rate should be between {low:.1f} and {high:.1f}")