def countWays(arr, m, N): 
  
    count = [0 for i in range(N + 1)] 
      
    count[0] = 1
    
    for i in range(1, N + 1):
        attempt = 0
        for j in range(m):
            if (i >= arr[j] and attempt<=11):
                attempt = attempt + 1
                count[i] += count[i - arr[j]] 
      
    return count[N] 

if __name__ == "__main__" : 
	points = [i * j for i in range(1, 21) for j in range(1, 4)] + [25, 50]
	points.sort(reverse=True)
	n = len(points)
	current_score = int(input('Input:'))
	ans = countWays(points, n, current_score) 
	print(ans)