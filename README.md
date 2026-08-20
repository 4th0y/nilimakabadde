# Happy Birthday Site 🎉

A one-page Django birthday site: confetti-cannon hero, a scrapbook photo
timeline, an envelope you tap open to reveal a letter, an embedded Spotify
playlist, and a corkboard "wishing wall" where friends can pin their own
messages — all editable from the Django admin, no code required.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and
`http://127.0.0.1:8000/admin/` to manage content.

## Adding your content, in the admin

1. **Site config** — the one row here holds her name, the hero tagline,
   the letter title/body, and the Spotify embed URL. To get a Spotify embed
   URL: open the playlist in Spotify → Share → Embed playlist → copy the
   `src="..."` link (looks like
   `https://open.spotify.com/embed/playlist/XXXXXXXX`).
2. **Memories** — add one row per photo for the scrapbook timeline. Upload
   the photo, write a caption, and optionally a date label like "Summer
   2021". `order` controls the sequence (lower = earlier).
3. **Messages** — pre-seed a few friends' messages here, or let people add
   their own directly from the site's wishing-wall form. Uncheck "approved"
   to hide a note without deleting it.

## Notes

- Uploaded photos are stored in `media/`, served by Django's dev server
  automatically when `DEBUG = True`.
- To deploy for real (so she can open it from a link), you'll want a host
  like Railway, Render, or PythonAnywhere, a production database, and
  `DEBUG = False` with a real `SECRET_KEY` and `ALLOWED_HOSTS`. Ask me if
  you'd like help with that part.
- Everything is a single Django app (`party/`) so it's easy to read end to
  end: `models.py`, `views.py`, `forms.py`, `admin.py`, and the templates
  under `party/templates/party/`.
