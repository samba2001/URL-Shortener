from django.db import models


class URL(models.Model):
    original_url = models.URLField(max_length=1500, verbose_name="Original URL")
    shortened_url = models.CharField(max_length=200, unique=True, verbose_name="Shortened URL")
    creation_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Creation Timestamp")
    expiration_timestamp = models.DateTimeField(null=True, blank=True, verbose_name="Expiration Timestamp")

    def __str__(self):
        return self.shortened_url


class AccessLog(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name="access_logs")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Access Timestamp")
    ip_address = models.CharField(max_length=100, blank=True, verbose_name="IP Address")

    def __str__(self):
        return f"{self.url.shortened_url} accessed at {self.timestamp}"
