# A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:

# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.

# def normalize(d1,d2,d3):




# day1=list(map(int,input("Enter day1 email-ids").split(",")))
# day2=list(map(int,input("Enter day2 email-ids").split(",")))
# day3=list(map(int,input("Enter day3 email-ids").split(",")))

# scenario(day1,day2,day3)

def normalize(*days):
    """Normalize case and remove duplicates from each day's list."""
    return [set(email.lower().strip() for email in day) for day in days]

def scenario(day1, day2, day3):
    # Normalize and clean data
    day1, day2, day3 = normalize(day1, day2, day3)

    # Total unique attendees
    all_unique = day1 | day2 | day3

    # Attended all three days
    all_three = day1 & day2 & day3

    # Attended exactly one day
    only_day1 = day1 - (day2 | day3)
    only_day2 = day2 - (day1 | day3)
    only_day3 = day3 - (day1 | day2)
    exactly_one_day = only_day1 | only_day2 | only_day3

    # Pairwise overlaps
    d1_d2 = day1 & day2
    d2_d3 = day2 & day3
    d1_d3 = day1 & day3

    # Final report
    print("\n Final Report")
    print(f"Total unique attendees: {len(all_unique)}")
    print(f"Attended all three days ({len(all_three)}): {sorted(all_three)}")
    print(f"Attended exactly one day ({len(exactly_one_day)}): {sorted(exactly_one_day)}")
    print(f"Day1 & Day2 overlap ({len(d1_d2)}): {sorted(d1_d2)}")
    print(f"Day2 & Day3 overlap ({len(d2_d3)}): {sorted(d2_d3)}")
    print(f"Day1 & Day3 overlap ({len(d1_d3)}): {sorted(d1_d3)}")

# Input section
day1 = input("Enter Day 1 email IDs (comma-separated): ").split(",")
day2 = input("Enter Day 2 email IDs (comma-separated): ").split(",")
day3 = input("Enter Day 3 email IDs (comma-separated): ").split(",")

scenario(day1, day2, day3)
