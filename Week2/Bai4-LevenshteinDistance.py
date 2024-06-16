def levenshtein_distance(token1, token2):
    # Your Code Here
  distance = 0
  m = len(token1)
  n = len(token2)
  ld = [[0]*(n+1) for _ in range(m+1)]
  for i in range(m+1):
    ld[i][0] = i
  for i in range(n+1):
    ld[0][i] = i

  for i in range(1, m+1):
    for j in range(1, n+1):
      ld[i][j] = min(ld[i-1][j]+1, ld[i][j-1]+1, ld[i-1][j-1]+(token1[i-1]!=token2[j-1]))

  distance = ld[m][n]
  # End Code Here
  return distance

assert levenshtein_distance("hi","hello") == 4.0
print(levenshtein_distance ("con đường", "cân đường"))
