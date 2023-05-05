"""You are counting points for a basketball game, given the
amount of 2-pointers scored and 3-pointers scored, find the
final points for the team and return that value."""

def points_counter(mid_range, long_range):
    mid_range = mid_range * 2
    long_range = long_range * 3
    team_total = mid_range + long_range
    return f"The teams total points is {team_total}"

print(points_counter(2, 3))