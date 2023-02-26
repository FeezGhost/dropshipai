from django.db import models

# Create your models here.

class Product:
    def __init__(self, _product, _store_name, _platform, _username, _bio, _marketing_campaign, _web_design, _ad_idea, _scaling):
        product             = _product
        store_name          = _store_name
        platform            = _platform
        username            = _username
        bio                 = _bio
        marketing_campaign  = _marketing_campaign
        web_design          = _web_design
        ad_idea             = _ad_idea
        scaling             = _scaling
        pass