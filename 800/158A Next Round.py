n, k = map(int, input().split())
scores = list(map(int, input().split()))
k_th_score = scores[k - 1]
advancers = 0
for score in scores:
  if score >= k_th_score and score > 0:
    advancers += 1
print(advancers)
