#include<bits/stdc++.h>
#include<iostream>
#include<chrono>
#include<algorithm>
#include<vector>

using namespace std;

int main()

{
    uint64_t key;
    string value;
    int n = 0;
    vector< pair <uint64_t,string>> vect;
    while (cin >> key >> value) {
        vect.push_back( make_pair(key,value) );
        n++;
    }
    using std::chrono::steady_clock;
    steady_clock::time_point start = steady_clock::now();
    stable_sort(vect.begin(), vect.end());
    steady_clock::duration dur = steady_clock::now() - start;
    std::cerr << "sort_time: " << std::chrono::duration_cast<std::chrono::milliseconds>(dur).count() << "ms\n";
    return 0;

}