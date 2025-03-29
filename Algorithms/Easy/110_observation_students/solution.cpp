#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> events;
    
    for (int i = 0; i < m; ++i) {
        int b1, b2;
        cin >> b1 >> b2;
        events.emplace_back(b1, 0);
        events.emplace_back(b2, 1);
    }
    
    events.emplace_back(n + 1, 0);
    events.emplace_back(n + 1, 1);
    
    sort(events.begin(), events.end());
    
    int prev = 0;
    int s = 0;
    int active_segments = 0;
    
    for (const auto& event : events) {
        int point = event.first;
        int event_type = event.second;
        
        if (active_segments == 0) {
            s += point - prev - 1;
        }
        if (event_type == 1) {
            prev = point;
            active_segments -= 1;
        } else {
            active_segments += 1;
        }
    }
    
    cout << s << endl;

    return 0;
}