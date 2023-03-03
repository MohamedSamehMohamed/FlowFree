#include<bits/stdc++.h>
using namespace std;
struct Grid{
	int x, y;
	int r, g, b; 
	bool taken = false; 
	bool operator==(Grid other)
	{
		return other.r == r && 
			   other.g == g && 
			   other.b == b; 
	} 
	bool empty()
	{
		return r + g + b == 0; 
	}
};
const int N = 10;
int n, m;
Grid grid[10][10];
vector<array<int, 4>> pairs;
vector<array<int, 3>> solution; 
bool vis[N][N]; 
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
bool solve(int index = 0, int cx = 0, int cy = 0, int tx = -1, int ty = -1)
{

	if (cx == tx && cy == ty)
	{
		if (index == pairs.size() - 1)
			return 1;
		solution.push_back({-1, -1, -1});
		solution.push_back({pairs[index+1][0], pairs[index+1][1], -1}); 
		if (solve(index+1, pairs[index+1][0], pairs[index+1][1], pairs[index+1][2], pairs[index+1][3]))
			return 1; 
		solution.pop_back();
		solution.pop_back(); 
		return 0; 
	}
	for(int k = 0; k < 4; k++)
	{
		int nx = cx + dx[k];
		int ny = cy + dy[k];
		if (min(nx, ny) < 0 || nx >= n || ny >= m || vis[nx][ny])continue; 
		if (!grid[nx][ny].empty())
		{
			if (nx != tx || ny != ty)
				continue; 
		}
		vis[nx][ny] = 1; 
		solution.push_back({nx, ny, -1}); 
		if (solve(index, nx, ny, tx, ty))
			return 1; 
		vis[nx][ny] = 0; 
		solution.pop_back(); 
	}
	return 0;

}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin >> n >> m;

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			cin >> grid[i][j].x >> grid[i][j].y >> grid[i][j].r >> grid[i][j].g >> grid[i][j].b; 
	
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			if (grid[i][j].empty() || grid[i][j].taken)
				continue; 
			for(int ii = 0; ii < n; ii++)
				for(int jj = 0; jj < m; jj++)
				{
					if (ii == i && jj == j)continue;
					if (grid[ii][jj].taken)continue;  
					if (!(grid[ii][jj] == grid[i][j]))continue; 
					pairs.push_back({i, j, ii, jj}); 
					grid[ii][jj].taken = grid[i][j].taken = 1; 
				}
		}	
	vis[pairs[0][0]][pairs[0][1]] = 1; 
	solution.push_back({pairs[0][0], pairs[0][1], -1}); 
	if (!solve(0, pairs[0][0], pairs[0][1], pairs[0][2], pairs[0][3]))
		cout <<"FAILD\n";

	for(auto i: solution)
		cout << i[0] <<" " << i[1] <<"\n"; 
}