from flask import Flask, render_template, request

app = Flask(__name__)

songs = [
    {
        "id": 1,
        "name": "Summer Vibes",
        "artist": "DJ Music",
        "album": "Summer Hits",
        "file": "song1.mp3"
    },
    {
        "id": 2,
        "name": "Night Drive",
        "artist": "Music World",
        "album": "Night Collection",
        "file": "song2.mp3"
    },
    {
        "id": 3,
        "name": "Dream Music",
        "artist": "John Beats",
        "album": "Dream Album",
        "file": "song3.mp3"
    }
]


@app.route("/")
def home():
    search = request.args.get("search", "").lower()

    filtered_songs = [
        song for song in songs
        if search in song["name"].lower()
        or search in song["artist"].lower()
    ]

    return render_template(
        "index.html",
        songs=filtered_songs
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
