playlist = [
    {"title": "Song A", "duration": 3},
    {"title": "Song B", "duration": 5},
    {"title": "Song C", "duration": 4}
]

def show_playlist():
    print("\n--- Playlist ---")
    for idx, song in enumerate(playlist):
        print(f"{idx+1}. {song['title']} ({song['duration']} min)")

def add_song():
    title = input("Enter song title: ")
    duration = int(input("Enter duration: "))
    playlist.append({"title": title, "duration": duration})
    print("Song added!")

def play_all():
    print("\nPlaying all songs:")
    for song in playlist:
        print(f"Now Playing: {song['title']}")

while True:
    print("\nOptions: 1-Show, 2-Add, 3-Play, 4-Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        show_playlist()
    elif choice == "2":
        add_song()
    elif choice == "3":
        play_all()
    elif choice == "4":
        break
    else:
        print("Invalid option")
