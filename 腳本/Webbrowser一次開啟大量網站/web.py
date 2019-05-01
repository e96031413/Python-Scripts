import webbrowser

with open("urls.txt") as f:
    for url in f:
        webbrowser.open_new_tab(url.strip())