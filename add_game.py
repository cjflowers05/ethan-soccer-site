#!/usr/bin/env python3
import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">
  <style>
    body {{ background: #121212; color: #fff; font-family: 'Poppins', sans-serif; margin: 0; }}
    header, footer {{ background: #1f1f1f; text-align: center; padding: 1rem; }}
    .container {{ max-width: 900px; margin: auto; padding: 1rem; }}
    .bio {{ background: #1e1e1e; padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem; }}
    a {{ color: #00ff7f; text-decoration: none; }}
    img, video {{ max-width: 100%; border-radius: 8px; margin-top: 1rem; }}
  </style>
</head>
<body>
<header>
  <h1>Ethan F. | Soccer Highlights</h1>
</header>
<div class="container">
  <h2>{title}</h2>
  <div class="bio">
    <p><strong>Game Summary:</strong> Add your recap here.</p>
  </div>
  <div class="bio">
    <h3>Photos</h3>
    <img src="../images/sample.jpg" alt="Game photo">
  </div>
  <div class="bio">
    <h3>Videos</h3>
    <video controls>
      <source src="../videos/sample.mp4" type="video/mp4" />
    </video>
  </div>
  <p><a href="../index.html">← Back to Home</a></p>
</div>
<footer><p>&copy; 2025 Ethan F. Soccer Highlights</p></footer>
</body>
</html>
"""

def generate_game_page(game_date, opponent, output_folder="games"):
    os.makedirs(output_folder, exist_ok=True)
    filename = f"{game_date}.html"
    title = f"{game_date.replace('-', '/')} - NCFC HSFV 2008 Gold vs {opponent}"
    content = TEMPLATE.format(title=title)
    path = os.path.join(output_folder, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"✔ Created {path}")

if __name__ == "__main__":
    print("Enter new game details:")
    date = input("Game date (YYYY-MM-DD): ").strip()
    opponent = input("Opponent name: ").strip()
    generate_game_page(date, opponent)
