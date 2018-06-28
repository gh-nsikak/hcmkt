#pip install beautifulsoup4
#pip install google

try:
  from google import search
except ImportError:
  print("No module name 'google' found")

# to search
query = "Geeksforgeeks"
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
  print(j)
