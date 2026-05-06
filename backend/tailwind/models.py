from django.db import models
from django.contrib.auth import get_user_model
from config.storage import upload_to
from utils.created_updated import CreatedUpdatedMixin
from django.core.exceptions import ValidationError

User = get_user_model()
    

class Portfolio(CreatedUpdatedMixin, models.Model):
    """Модель, представляющая портфолио с работами пользователя"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    is_commissioning_open = models.BooleanField(default=False, blank=False, null=False)
    description = models.TextField(max_length=3000, blank=False, null=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user"],
                name="unique_user_portfolio"
            )
        ]
    
    def __str__(self):
        return f"id: {self.id} | user: {self.user.get_full_name()}"

class Artwork(CreatedUpdatedMixin, models.Model):
    """Модель, представляющая работу в портфолио"""
    title = models.CharField(max_length=255, blank=False, null=False, help_text="Your artwork title")
    image = models.ImageField(db_comment="User artwork", upload_to=upload_to)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.DO_NOTHING, related_name="artworks")
    is_hidden = models.BooleanField(default=False)
    is_subscription_needed = models.BooleanField(default=False)

    def __str__(self):
        return f"id: {self.id} | title: {self.title} | portfolio_id: {self.portfolio.id}"

class Subscriber(models.Model):
    """Модель, представляющая подписчику юзера на портфолио"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.DO_NOTHING, related_name="subscribers")

    def clean(self):
        if self.user_id == self.portfolio.user_id:
            raise ValidationError("User cannot subscribe to their own portfolio")
        
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "portfolio"],
                name="unique_user_portfolio_subscriber"
            ),
        ]

class Comment(CreatedUpdatedMixin, models.Model):
    """Модель, представляющая связанный с работой комментарий"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="comments")
    artwork = models.ForeignKey(Artwork, on_delete=models.DO_NOTHING, related_name="comments")
    text = models.TextField(max_length=2000, blank=False, null=False, default="")

class Like(models.Model):
    """Модель, представляющая оценку работы"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    artwork = models.ForeignKey(Artwork, on_delete=models.DO_NOTHING, related_name="likes")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "artwork"],
                name="unique_user_artwork_like"
            )
        ]