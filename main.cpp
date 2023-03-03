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
Grid grid[N][N];
vector<array<int, 4>> pairs;
vector<array<int, 3>> solution; 
bool vis[N][N]; 
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int temp_vis[N][N];
void init_temp_vis(){
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			temp_vis[i][j] = vis[i][j];
}
bool canReach(int srcX, int srcY, int targetX, int targetY){
	if (srcX == targetX && srcY == targetY) 
		return 1;
	temp_vis[srcX][srcY] = 1;
	for(int k = 0; k < 4; k++)
	{
		int nx = srcX + dx[k];
		int ny = srcY + dy[k];
		if (min(nx, ny) < 0 || nx >= n || ny >= m || temp_vis[nx][ny])continue; 
		// if this cell not empty it must be the target cell otherwise we can't visit it 
		if (!grid[nx][ny].empty())
		{
			if (nx != targetX || ny != targetY)
				continue; 
		}
		temp_vis[nx][ny] = 1; 
		if (canReach(nx, ny, targetX, targetY))
			return 1;  
	}
	temp_vis[srcX][srcY] = 0;
	return 0;
}
void dfs(int r, int c, int color){
	temp_vis[r][c] = color;
	for(int k = 0; k < 4; k++)
	{
		int nx = r + dx[k];
		int ny = c + dy[k];
		if (min(nx, ny) < 0 || nx >= n || ny >= m || temp_vis[nx][ny] || !grid[nx][ny].empty())continue; 
		dfs(nx, ny, color);
	}
}
bool canWeContinue(int index){
	init_temp_vis();
	int markColor = 2;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++){
			if (temp_vis[i][j] || !grid[i][j].empty()) continue;
			dfs(i, j, markColor);
			markColor++;
		}
	}
	while (index < pairs.size()){
		int msk1 = 0, msk2 = 0;
		for(int k = 0; k < 4; k++)
		{
			for (int j = 0; j <= 2; j+=2){
				int nx = pairs[index][0 + j] + dx[k];
				int ny = pairs[index][1 + j] + dy[k];
				if (min(nx, ny) < 0 || nx >= n || ny >= m || temp_vis[nx][ny] <= 1 || !grid[nx][ny].empty())
					continue; 
				if (j) 
					msk2 |= (1<<temp_vis[nx][ny]);
				else 
					msk1 |= (1<<temp_vis[nx][ny]);
			}
		}
		bool match = 0;
		for (int i = 2; i <= markColor; i++){
			if ((msk1 & (1<<i)) && (msk2 & (1<<i))){
				match = 1;
				break;
			}
		}
		if (!match) 
			return 0;
		index++;
	}
	return 1;
}
bool solve(int index = 0, int cx = 0, int cy = 0, int tx = -1, int ty = -1)
{
	// if src == target 
	if (cx == tx && cy == ty)
	{
		// if we end the pairs list , we are finished 
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
	if (!canWeContinue(index+1)) 
		return 0;
	for(int k = 0; k < 4; k++)
	{
		int nx = cx + dx[k];
		int ny = cy + dy[k];
		if (min(nx, ny) < 0 || nx >= n || ny >= m || vis[nx][ny])continue; 
		// if this cell not empty it must be the target cell otherwise we can't visit it 
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
	else 
		{
			for(auto i: solution)
				cout << i[0] <<" " << i[1] <<"\n"; 
		}
}