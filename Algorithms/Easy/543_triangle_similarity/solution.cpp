// Solution for https://coderun.yandex.ru/problem/triangle-similarity/

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <tuple>

// Calculate greatest common divisor
int gcd(int a, int b) {
    while (b) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

// Calculate GCD for three numbers
int gcd_three(int a, int b, int c) {
    return gcd(a, gcd(b, c));
}

// Normalize triangle by dividing all sides by their GCD
std::tuple<int, int, int> normalize_triangle(std::vector<int>& sides) {
    // Sort sides to ensure consistent ordering
    std::sort(sides.begin(), sides.end());
    
    // Find GCD of all three sides
    int g = gcd_three(sides[0], sides[1], sides[2]);
    
    // Return normalized sides as a tuple (for hashing)
    return std::make_tuple(sides[0] / g, sides[1] / g, sides[2] / g);
}

int main() {
    int n;
    std::cin >> n;
    
    std::set<std::tuple<int, int, int>> unique_triangles;
    
    for (int i = 0; i < n; i++) {
        std::vector<int> sides(3);
        std::cin >> sides[0] >> sides[1] >> sides[2];
        
        auto normalized = normalize_triangle(sides);
        unique_triangles.insert(normalized);
    }
    
    std::cout << unique_triangles.size() << std::endl;
    
    return 0;
}