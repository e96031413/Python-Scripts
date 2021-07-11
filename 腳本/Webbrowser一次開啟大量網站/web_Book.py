import webbrowser

with open("book_url.txt") as f:
    for url in f:
        webbrowser.open_new_tab(url.strip())