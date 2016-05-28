from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
# Create your models here.
# verbose_name

class Category(models.Model):
    TYPE_CHOICES = (
     (1, _('public category')),
     (2, _('news category')),
     (3, _('product category')),
    )
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children",verbose_name=_('parent category'))
    category_type = models.PositiveSmallIntegerField(_('category type'), choices=TYPE_CHOICES, default=1)
    title = models.CharField(_('category title'), max_length=50)
    create_time = models.DateTimeField(verbose_name=_('category create time'))
    description = models.TextField(_('category description'),blank=True)
    slug = models.SlugField(_('slug title'), help_text=_('Use ascii characters'))
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='category/photos/%Y/%m/%d/%H/%M/')
    is_enable = models.BooleanField(_('enable'), default=False)

    class Meta:
        db_table = "categories"
        verbose_name = "category"
        ordering = ["title", "id"]

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('product title'), max_length=50)
    create_time = models.DateTimeField(verbose_name=_('product create time'), auto_now_add=True)
    slug = models.SlugField(_('slug title'), help_text=_('Use ascii characters'))
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children",verbose_name=_('parent product'))
    category = models.ManyToManyField(Category, verbose_name=_('categories'),related_name='categories', blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/photos/%Y/%m/%d/%H/%M/')
    is_enable = models.BooleanField(_('enable'), default=False)

    class Meta:
        db_table = "products"
        ordering = ["title", "id"]

    def __str__(self):
        return self.title



class ProductImages(models.Model):
    created_time = models.DateTimeField(_('creation time'), auto_now_add=True)
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='photos', null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(_('uploaded photo'), upload_to='productsimages/photos/%Y/%m/%d/%H/%M/')
    is_enable = models.BooleanField(_('enable'), default=False)

    class Meta:
        db_table = "products_image"
        ordering = ["created_time", "product", "id"]
    def __str__(self):
        return '%s-%s' % (self.product, self.id)
