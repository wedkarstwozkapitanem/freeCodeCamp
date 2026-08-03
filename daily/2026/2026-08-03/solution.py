def get_emoji_phrase(s):
    slownik = {
        "👶":"baby",
        "🐱":"cat",
        "🐕":"dog",
        "🐟":"fish",
        "🥵":"hot",
        "🧊":"ice",
        "🪨":"rock",
        "🦈":"shark",
        "🍲":"soup",
        "⭐":"star"
    }

    return " ".join([slownik[i] for i in s])

print(get_emoji_phrase("⭐🐟"))