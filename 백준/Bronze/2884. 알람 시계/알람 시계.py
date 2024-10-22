h, m = map(int, input().split())

if m >= 45:
  print (h, m - 45)
elif m < 45:
  h = h - 1
  if h < 0 :
    h = h + 24
  print (h , m + 60 - 45)
