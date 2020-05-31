
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

using std::vector;

struct DisjointSet {
  vector<int> parent;
  vector<int> rank;

  DisjointSet(int n): parent(n), rank(n)  {
    for(int i = 0; i < n; ++i)
      parent[i] = i;
  }

  int find_parent(int i) {
    while(i != parent[i])
      i = parent[i];
    return i;
  }

  void unite_sets(int i, int j) {
    int i_id = find_parent(i);
    int j_id = find_parent(j);

    if(i_id == j_id)
        return;
    if(rank[i_id] > rank[j_id])
        parent[j_id] = i_id;
    else {
      parent[i_id] = j_id;
      if(rank[i_id] == rank[j_id])
        rank[j_id]++;
    }
  }
};

struct Edge {
  int u, v;
  double dist{-1};
  Edge(int u, int v, double dist): u(u), v(v), dist(dist) {}
};

bool operator < (Edge &a, Edge &b){
  return a.dist < b.dist;
}

double compute_dist(int x1, int y1, int x2, int y2) {
  return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

double minimum_distance(vector<Edge> &Es, DisjointSet &ds) {
  std::sort(Es.begin(), Es.end());
  ds.unite_sets(Es[0].u, Es[0].v);
  double result = Es[0].dist;
  for(auto &edge: Es) {
    if(ds.find_parent(edge.u) != ds.find_parent(edge.v)) {
      result += edge.dist;
      ds.unite_sets(edge.u, edge.v);
    }
  }
  return result;
}

int main() {
  size_t n;
  std::cin >> n;
  vector<int> x(n), y(n);
  vector<Edge> edges;
  DisjointSet ds(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> x[i] >> y[i];
    for(size_t j = 0; j != i; ++j)
         edges.push_back(Edge(i, j, compute_dist(x[i], y[i], x[j], y[j])));
  }
  std::cout << std::setprecision(10) << (n < 2 ? 0.000000000 : minimum_distance(edges, ds)) << std::endl;
}