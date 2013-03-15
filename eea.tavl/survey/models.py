from django.db import models
from django_hstore import hstore


WIDGETS = {
    'section_a': 'SectionA',
    'section_a_info': 'SectionAInfo',
    'section_a_comment': 'SectionAComment',
    'section_b': 'SectionB',
    'section_b_4': 'SectionB4',
    'section_b_info': 'SectionBInfo',
    'section_b_comment': 'SectionBComment',
    'section_c': 'SectionC',
    'section_c_1_h': 'SectionC1Other',
    'section_c_2': 'SectionC2',
    'section_c_3': 'SectionC3',
    'section_c_comment': 'SectionCComment',
    'section_e_comment': 'SectionEComment',
    'section_e': 'SectionE',
    'section_d_1': 'SectionD1',
    'section_d1_other': 'SectionD1Other',
    'section_d2_other': 'SectionD2Other',
    'section_d_2': 'SectionD2',
    'section_d2_comment': 'SectionDComment',
}


class Section(models.Model):

    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'section'

    def __unicode__(self):
        return self.name


class Category(models.Model):

    title = models.CharField(max_length=256)

    description = models.CharField(max_length=2056)

    section = models.ForeignKey(Section)

    widget = models.CharField(max_length=32)

    for_user = models.BooleanField(default=False)

    multiple_answers = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'
        ordering = ['pk']

    def __unicode__(self):
        return self.title or ''

    def get_widget(self):
        from survey import forms
        widget = getattr(forms, WIDGETS[self.widget])
        return widget


class Language(models.Model):

    iso = models.CharField(max_length=3, primary_key=True)

    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'language'


class Survey(models.Model):

    class Meta:
        db_table = 'survey'

    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('in_planning', 'In planning'),
        ('not_available', 'Not available'),
    )

    TRANSPORT_PARTS = (
        ('infrastructure', 'Transport infrastructure'),
        ('services', 'Transport services'),
    )

    TRANSPORT_MODES = (
        ('road', 'Road'),
        ('rail', 'Rail'),
        ('aviation', 'Aviation'),
        ('inland_water', 'Inland water shipping'),
        ('maritime', 'Maritime shipping'),
        ('urban_transport', 'Urban transport'),
    )

    IMPACTS = (
        ('temperatures', '(Extreme) Temperatures'),
        ('flooding', 'Flooding'),
        ('sea_level_rise', 'Sea level rise'),
        ('storms', 'Storms'),
        ('ice_snow', 'Ice and snow'),
        ('water_scarcity_droughts', 'Water scarcity and droughts'),
    )

    RELEVANT_CHOICES = (
        ('none', 'None'),
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
        ('don\'t know', 'don\'t know'),
    )

    category = models.ForeignKey(Category)

    country = models.ForeignKey('countries.Country')

    user = models.ForeignKey('tach.User')

    date = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    title = models.CharField(max_length=256, null=True, blank=True)

    english_title = models.CharField(max_length=256, null=True, blank=True)

    year = models.IntegerField(null=True, blank=True)

    parts_considered = hstore.DictionaryField(null=True, blank=True )

    transport_modes = hstore.DictionaryField(null=True, blank=True)

    climate_change_impacts = hstore.DictionaryField(null=True, blank=True)

    responsible_organisation = models.CharField(max_length=256, null=True,
                                                blank=True)

    link = models.CharField(max_length=256, null=True, blank=True)

    language = models.ForeignKey(Language, null=True, blank=True)

    contact = models.CharField(max_length=256, null=True, blank=True)

    focus = models.CharField(max_length=256, null=True, blank=True)

    section_a_info = models.TextField(null=True, blank=True)

    section_a_comment = models.TextField(null=True, blank=True)

    section_b_info = models.TextField(null=True, blank=True)

    section_b_comment = models.TextField(null=True, blank=True)

    section_c2 = models.TextField(null=True, blank=True)

    section_d_comment = models.TextField(null=True, blank=True)

    section_c_comment = models.TextField(null=True, blank=True)

    section_e_comment = models.TextField(null=True, blank=True)

    area_of_expertise = models.CharField(max_length=256, null=True, blank=True)

    # section D

    adaptation_strategy = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    transport_information = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    trans_national_cooperation = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    stakeholders_cooperaton = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    integration_of_climate_change = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    funding = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    revision_of_design = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    climate_proof = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    development_methodologies = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    data_collection = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    transport_research = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    lack_of_awareness = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    knowledge_gaps = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    data_gaps = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    lack_of_training = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    lack_of_capacities = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    lack_of_resources = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    access_to_funding = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    lack_of_coordination = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    awareness_lack_eu_level = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True,
                            blank=True)

    relevance = models.CharField(max_length=50, choices=RELEVANT_CHOICES, null=True, blank=True)

    d1_comments = models.TextField(null=True, blank=True)

    d2_comments = models.TextField(null=True, blank=True)

    objects = hstore.HStoreManager()
