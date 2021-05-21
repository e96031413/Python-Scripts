import webbrowser

with open("urls_FB.txt") as f:
    for url in f:
        webbrowser.open_new_tab(url.strip())
