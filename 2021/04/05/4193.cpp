/*
SWEA 4193 수영대회 결승전
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWKaG6_6AGQDFARV&categoryId=AWKaG6_6AGQDFARV&categoryType=CODE
*/
// BFS
// Djikstra 도 가능하다함
#include <iostream>
#include <queue>
#include <tuple>
#include <cmath>
#include <cstring>
using namespace std;

int main(int argc, char** argv)
{
	int test_case, N;
	int A, B, C, D;
	int T, answer;
	int board[15][15];
	int visited[15][15];
	int dy[4] = {0, 0, 1, -1};
	int dx[4] = {1, -1, 0, 0};
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		for(int y = 0;y<N;y++)
			for(int x = 0; x<N; x++)
				cin >> board[y][x];
		cin >> A >> B;
		cin >> C >> D;
		memset(visited, 0, sizeof(int) *15 * 15);
		answer = (int)pow(N, 2);
		queue< tuple<int, int ,int> > q = queue<tuple<int, int ,int>>();
		q.push(make_tuple(A, B, 0));
		while(!q.empty())
		{
			int y = get<0>(q.front()), x = get<1>(q.front()), time = get<2>(q.front());
			q.pop();

			visited[y][x] = 1;
			if (y == C && x == D)
			{
				cout << "[" << y << ", " << x << " - " << time << "]" << endl;
				answer = answer > time ? time : answer;
				continue;
			}

			for(int i=0; i<4; i++)
			{
				int nx = x + dx[i], ny = y + dy[i];
				if (ny < 0 || ny >= N)
					continue;
				if (nx < 0 || nx >= N)
					continue;
				if (board[ny][nx] == 1)
					continue;
				if (!visited[ny][nx])
				{
					int next = time;
					if (board[ny][nx] == 2 && (next - 2) % 3 != 0)
					{
						while ((next - 2) % 3 != 0)
							next++;
					}
					q.push(make_tuple(ny, nx, next + 1));
				}
			}
		}
		if (answer == (int)pow(N ,2))
			answer = -1;
		cout << "#" << test_case << " " << answer << endl;
	}
	return 0;
}