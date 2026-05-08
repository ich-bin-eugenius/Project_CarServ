from django.db import models


# ------------About------------

class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    experience_years = models.IntegerField(default=0)
    experience_text = models.CharField(max_length=50, default="Years Experience")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class AboutFeature(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="features")
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"


# ------------Contact------------

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'


class MessageFromCustomer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'Message from Customer'
        verbose_name_plural = 'Messages from Customers'


class ContactInfo(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    work_schedule = models.CharField(max_length=100)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


# ------------Home------------

class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    years_experience = models.CharField(max_length=255, default=0)
    expert_technicians = models.CharField(max_length=255, default=0)
    satisfies_clients = models.CharField(max_length=255, default=0)
    compleate_projects = models.CharField(max_length=255, default=0)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Establishments'


# ------------Services------------

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Services'
