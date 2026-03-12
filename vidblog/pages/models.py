from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")
    slug = models.SlugField(unique=True, help_text="Link ID")

    class Meta:
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name

class video(models.Model): # يفضل يبدأ بحرف كبير Video
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    link = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True) # خليه تلقائي أسهل
    # حدد مجلد للرفع ومسموح يكون فاضي لو هتستخدم الرابط الخارجي
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True) 
    external_thumbnail_url = models.URLField(blank=True, null=True, verbose_name="رابط صورة خارجية")
    slug = models.SlugField(unique=True)
    time = models.TimeField()
    views = models.PositiveIntegerField(default=0, verbose_name="views count")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title if self.title else "Untitled Video"

@property
def smart_thumbnail(self):
        # 1. لو فيه صورة مرفوعة محلياً، استخدمها
    if self.thumbnail:
        return self.thumbnail.url
        # 2. لو مفيش، استخدم الرابط الخارجي
    if self.external_thumbnail_url:
        return self.external_thumbnail_url
        # 3. لو مفيش الاتنين، رجع رابط صورة "قريباً" أو صورة افتراضية
    return "/static/images/no-image.png"