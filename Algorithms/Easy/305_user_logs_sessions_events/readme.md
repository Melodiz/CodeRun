# [305. Пользовательские логи](https://coderun.yandex.ru/problem/user-logs-sessions-events)

## 📋 Problem Description

This problem involves analyzing user activity logs stored in `log.csv`. Each line represents a single event with the format:
```
timestamp,user_id,event_type,event_parameter
```

## 🎯 Tasks

### 1. Session Counting
- **Definition**: A session is a sequence of events by the same user
- **Session End Rule**: Session ends after 30+ minutes of inactivity
- **Goal**: Count sessions that **started** on `2020-04-19`

### 2. Most Active Video Day
- **Video Event**: `event_type = 2` and `event_parameter = "video"`
- **Goal**: Find the day with the **maximum number of unique users** who watched videos
- **Return**: The count of unique users (not the date)

### 3. Most Active 5-Minute Interval
- **Goal**: Find the 5-minute interval `[time, time + 5 minutes)` with the most events
- **Tie-breaker**: If multiple intervals have the same count, return the **latest** one
- **Return**: Start time in format `YYYY-MM-DD_hh:mm:ss`

## 🔧 Solution Approach

### Session Counting Algorithm
1. Group events by user_id and sort by timestamp
2. For each user, identify session start points:
   - First event starts a session
   - Any event after a 30+ minute gap starts a new session
3. Count sessions that started on the target date

### Video Day Analysis
1. Filter events with `type=2` and `parameter="video"`
2. Group by date and collect unique user_ids per day
3. Return the maximum count of unique users

### Active Interval Detection
1. Sort all timestamps chronologically
2. Use sliding window approach to check each possible 5-minute interval
3. Count events in each window and track the best (preferring later times for ties)

## 📊 Output Format

```
<session_count> <max_unique_users> <interval_start_time>
```

**Example**: `67890 111 2020-01-31_10:09:12`

## 🚀 Usage

```bash
python solution.py
```

**Prerequisites**: 
- `log.csv` file in the same directory
- Python 3.6+ with `datetime` module

## 🏷️ Tags
- Data Analysis
- Log Processing  
- Time Series Analysis
- Sliding Window Algorithm
- Session Management

## 📈 Complexity
- **Time**: O(n log n) due to sorting operations
- **Space**: O(n) for storing user activities and timestamps

## 🔗 Links
- [Original Problem](https://coderun.yandex.ru/problem/user-logs-sessions-events)
- [More Solutions](https://github.com/Melodiz/CodeRun)

