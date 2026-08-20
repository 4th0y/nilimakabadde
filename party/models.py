from django.core.exceptions import ValidationError
from django.db import models


class SiteConfig(models.Model):
    """Singleton-style config: only one row should ever exist.
    Edit it in the Django admin to change the friend's name, the
    letter, and the music embed without touching any code."""

    friend_name = models.CharField(
        max_length=100, default="Friend",
        help_text="Shown in the big hero headline, e.g. 'Priya'."
    )
    hero_tagline = models.CharField(
        max_length=200, blank=True,
        default="Press the button. Things will happen.",
        help_text="Small line under the headline."
    )
    letter_title = models.CharField(max_length=150, default="A letter for you")
    letter_body = models.TextField(
        blank=True,
        help_text="Your birthday letter. Line breaks are preserved."
    )
    spotify_embed_url = models.URLField(
        blank=True,
        help_text=(
            "Paste a Spotify EMBED url, e.g. "
            "https://open.spotify.com/embed/playlist/XXXXXXXX. "
            "In Spotify: Share -> Embed playlist -> copy the src=\"...\" link."
        ),
    )

    class Meta:
        verbose_name = "Site config"
        verbose_name_plural = "Site config (edit the one row)"

    def clean(self):
        if not self.pk and SiteConfig.objects.exists():
            raise ValidationError(
                "Only one Site config row is allowed. Edit the existing one."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Site config for {self.friend_name}"

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Memory(models.Model):
    """One entry in the photo timeline."""

    photo = models.ImageField(upload_to="memories/")
    caption = models.CharField(max_length=200)
    date_label = models.CharField(
        max_length=50, blank=True,
        help_text="Free text, e.g. 'Summer 2021' or 'The day we met'."
    )
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers show first."
    )

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.caption


class Message(models.Model):
    """A birthday note left by a friend, shown on the messages wall."""

    name = models.CharField(max_length=80)
    message = models.TextField(max_length=500)
    color = models.CharField(
        max_length=20,
        choices=[
            ("pink", "Pink"),
            ("yellow", "Yellow"),
            ("blue", "Blue"),
            ("purple", "Purple"),
        ],
        default="pink",
        help_text="Sticky-note color on the wall.",
    )
    approved = models.BooleanField(
        default=True,
        help_text="Uncheck to hide a message without deleting it.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.name}: {self.message[:30]}"
