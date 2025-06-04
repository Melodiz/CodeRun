# Solution for https://coderun.yandex.ru/problem/user-logs-sessions-events
# Other solutions: https://github.com/Melodiz/CodeRun
from datetime import datetime, timedelta

def count_sessions(logs):
    """Count sessions that started on 2020-04-19"""
    target_date = datetime.strptime("2020-04-19", "%Y-%m-%d").date()
    users_activities = {}
    
    # Group logs by user_id and convert to datetime
    for log in logs:
        date, user_id, event_type, parameter = log.split(',')
        dt = datetime.strptime(date, "%Y-%m-%d_%H:%M:%S")
        if user_id not in users_activities:
            users_activities[user_id] = []
        users_activities[user_id].append(dt)
    
    sessions = 0
    for user_id, activities in users_activities.items():
        activities.sort()
        
        # Find session boundaries for this user
        session_starts = []
        if activities:
            session_starts.append(activities[0])  # First activity starts a session
        
        # Find additional session starts (after 30+ minute gaps)
        for i in range(1, len(activities)):
            if activities[i] - activities[i-1] >= timedelta(minutes=30):
                session_starts.append(activities[i])
        
        # Count sessions that started on target date
        for session_start in session_starts:
            if session_start.date() == target_date:
                sessions += 1
    
    return sessions

def find_most_viewed_day(logs):
    """Find day with maximum unique users who watched videos"""
    daily_users = {}  # date -> set of user_ids
    
    for log in logs:
        date, user_id, event_type, parameter = log.split(',')
        if event_type == "2" and parameter == "video":
            dt = datetime.strptime(date, "%Y-%m-%d_%H:%M:%S")
            date_str = dt.strftime("%Y-%m-%d")
            
            if date_str not in daily_users:
                daily_users[date_str] = set()
            daily_users[date_str].add(user_id)
    
    # Find day with most unique users
    max_users = 0
    best_day = None
    for day, users in daily_users.items():
        if len(users) > max_users:
            max_users = len(users)
            best_day = day
    
    return max_users

def find_most_active_interval(logs):
    """Find 5-minute interval with most events"""
    # Extract and sort all timestamps
    timestamps = []
    for log in logs:
        date, user_id, event_type, parameter = log.split(',')
        timestamps.append(datetime.strptime(date, "%Y-%m-%d_%H:%M:%S"))
    
    timestamps.sort()
    
    max_events = 0
    best_start_time = None
    
    # Use sliding window approach
    for i in range(len(timestamps)):
        start_time = timestamps[i]
        end_time = start_time + timedelta(minutes=5)
        
        # Count events in this 5-minute window
        events_count = 0
        for j in range(i, len(timestamps)):
            if timestamps[j] < end_time:
                events_count += 1
            else:
                break
        
        # Update best interval (prefer later time if tied)
        if events_count > max_events or (events_count == max_events and start_time > best_start_time):
            max_events = events_count
            best_start_time = start_time
    
    return best_start_time.strftime("%Y-%m-%d_%H:%M:%S")

def main():
    """Main function to read logs and solve all three problems"""
    data = []
    with open("log.csv", "r") as file:
        for line in file:
            data.append(line.strip())
    
    # Skip header if present
    if data and (data[0].startswith('date') or data[0].startswith('time')):
        data = data[1:]
    
    sessions = count_sessions(data)
    most_viewed_day_count = find_most_viewed_day(data)
    most_active_interval = find_most_active_interval(data)
    
    # Output in required format: sessions, max_users, interval_start
    print(f"{sessions} {most_viewed_day_count} {most_active_interval}")

if __name__ == "__main__":
    main()
