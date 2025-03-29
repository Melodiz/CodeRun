#include <cmath>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

// Function to generate a random point in a unit cube
vector<double> generate_random_point()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);

    double x = dis(gen);
    double y = dis(gen);
    double z = dis(gen);

    return {x, y, z};
}

double euclidean_distance(double x1, double y1, double z1, double x2, double y2, double z2)
{
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1);
}

bool checkIfFarEnough(vector<double>& point, double radius)
{
    double x = point[0];
    double y = point[1];
    double z = point[2];
    // check if the point is far enough from (0,0,0)
    if (euclidean_distance(x, y, z, 0.0, 0.0, 0.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 1.0, 0.0, 0.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 0.0, 1.0, 0.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 0.0, 0.0, 1.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 1.0, 1.0, 0.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 1.0, 0.0, 1.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 0.0, 1.0, 1.0) <= radius) { return false;}
    if (euclidean_distance(x, y, z, 1.0, 1.0, 1.0) <= radius) { return false;}
    return true;
}

int main()
{
    const int num_samples = 1e6;
    int count = 0;
    double radius = pow(3.0/4.0, 2);

    for (int i = 0; i < num_samples; ++i)
    {
        vector<double> point = generate_random_point();
        if (checkIfFarEnough(point, radius))
        {
            count++;
        }
    }

    double probability = static_cast<double>(count) / num_samples;
    cout << "Probability: " << probability << endl;

    return 0;
}