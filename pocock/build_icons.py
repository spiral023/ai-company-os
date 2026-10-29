"""Standardgrößen aus dem Imagegen-Original ableiten; Bildmotiv unverändert lassen."""
from pathlib import Path

from PIL import Image

APP = Path(__file__).resolve().parent


def build():
    public = APP / "public"
    icons = public / "icons"
    icons.mkdir(parents=True, exist_ok=True)
    with Image.open(APP / "assets/portrait-source.png") as original:
        if original.width != original.height:
            raise ValueError("Ein quadratisches Icon-Original ist erforderlich.")
        image = original.convert("RGB")
        for name, size in [("favicon-16-v1", 16), ("favicon-32-v1", 32), ("apple-touch-icon-v1", 180), ("icon-192-v1", 192), ("icon-512-v1", 512)]:
            image.resize((size, size), Image.Resampling.LANCZOS).save(icons / (name + ".png"), optimize=True)
        image.save(public / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("App-Icons, Apple-Touch-Icon und mehrstufiges Favicon erzeugt.")


if __name__ == "__main__":
    build()
