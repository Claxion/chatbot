import webbrowser

url = "https://search.daum.net/search?q="
keywords = ["아이유","설현","박보영"]
for keyword in keywords:
    webbrowser.open(url+keyword)