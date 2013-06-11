from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from flis import models, auth, forms


PER_PAGE = 25


class BaseQuerysetView(object):

    def get_queryset(self):
        return self.model.objects.filter(country=self.request.country)


#Interlink
class Interlinks(BaseQuerysetView, ListView):

    model = models.Interlink
    template_name = 'interlinks/interlinks.html'
    paginate_by = PER_PAGE

    def get_queryset(self):
        return self.model.objects.filter(country=self.request.country)


class Interlink(BaseQuerysetView, DetailView):

    model = models.Interlink
    template_name = 'interlinks/interlink.html'
    paginate_by = PER_PAGE


class InterlinkCreate(CreateView):

    model = models.Interlink
    template_name = 'interlinks/interlink_edit.html'
    form_class = forms.InterlinkForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(InterlinkCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('interlinks', kwargs={'country': country})
        return context


class InterlinkEdit(BaseQuerysetView, UpdateView):

    model = models.Interlink
    template_name = 'interlinks/interlink_edit.html'
    form_class = forms.InterlinkForm

    def get_context_data(self, *args, **kwargs):
        context = super(InterlinkEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class InterlinkDelete(BaseQuerysetView, DeleteView):

    model = models.Interlink

    def get_success_url(self):
        country = self.request.country
        return reverse('interlinks', kwargs={'country': country})


#Sources
class Sources(BaseQuerysetView, ListView):

    model = models.Source
    template_name = 'sources/sources.html'
    paginate_by = PER_PAGE


class Source(BaseQuerysetView, DetailView):

    model = models.Source
    template_name = 'sources/source.html'


class SourceCreate(CreateView):

    template_name = 'sources/source_edit.html'
    model = models.Source
    form_class = forms.SourceForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(SourceCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('sources', kwargs={'country': country})
        return context


class SourceEdit(BaseQuerysetView, UpdateView):

    template_name = 'sources/source_edit.html'
    model = models.Source
    form_class = forms.SourceForm

    def get_context_data(self, *args, **kwargs):
        context = super(SourceEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SourceDelete(BaseQuerysetView, DeleteView):

    model = models.Source

    def get_success_url(self):
        country = self.request.country
        return reverse('sources', kwargs={'country': country})


#GMT
class GMTs(BaseQuerysetView, ListView):

    model = models.GMT
    template_name = 'gmt/gmts.html'
    paginate_by = PER_PAGE


class GMT(BaseQuerysetView, DetailView):

    model = models.GMT
    template_name = 'gmt/gmt.html'


class GMTCreate(CreateView):

    model = models.GMT
    template_name = 'gmt/gmt_edit.html'
    form_class = forms.GMTForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(GMTCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('gmts', kwargs={'country': country})
        return context


class GMTEdit(BaseQuerysetView, UpdateView):

    model = models.GMT
    template_name = 'gmt/gmt_edit.html'
    form_class = forms.GMTForm

    def get_context_data(self, *args, **kwargs):
        context = super(GMTEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GMTDelete(BaseQuerysetView, DeleteView):

    model = models.GMT

    def get_success_url(self):
        country = self.request.country
        return reverse('gmts', kwargs={'country': country})

#Models
class FlisModels(BaseQuerysetView, ListView):

    model = models.FlisModel
    template_name = 'flismodel/flismodels.html'
    paginate_by = PER_PAGE


class FlisModel(BaseQuerysetView, DetailView):

    model = models.FlisModel
    template_name = 'flismodel/flismodel.html'


class FlisModelCreate(CreateView):

    model = models.FlisModel
    template_name = 'flismodel/flismodel_edit.html'
    form_class = forms.FlisModelForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(FlisModelCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('flismodels', kwargs={'country': country})
        return context


class FlisModelEdit(BaseQuerysetView, UpdateView):

    model = models.FlisModel
    template_name = 'flismodel/flismodel_edit.html'
    form_class = forms.FlisModelForm

    def get_context_data(self, *args, **kwargs):
        context = super(FlisModelEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class FlisModelDelete(BaseQuerysetView, DeleteView):

    model = models.FlisModel

    def get_success_url(self):
        country = self.request.country
        return reverse('flismodels', kwargs={'country': country})


#Horizon Scanning
class HorizonScannings(BaseQuerysetView, ListView):

    model = models.HorizonScanning
    template_name = 'horizonscanning/horizonscannings.html'
    paginate_by = PER_PAGE


class HorizonScanning(BaseQuerysetView, DetailView):

    model = models.HorizonScanning
    template_name = 'horizonscanning/horizonscanning.html'


class HorizonScanningCreate(CreateView):

    model = models.HorizonScanning
    template_name = 'horizonscanning/horizonscanning_edit.html'
    form_class = forms.HorizonScanningForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(HorizonScanningCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('horizonscannings', kwargs={'country': country})
        return context


class HorizonScanningEdit(BaseQuerysetView, UpdateView):

    model = models.HorizonScanning
    template_name = 'horizonscanning/horizonscanning_edit.html'
    form_class = forms.HorizonScanningForm

    def get_context_data(self, *args, **kwargs):
        context = super(HorizonScanningEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class HorizonScanningDelete(BaseQuerysetView, DeleteView):

    model = models.HorizonScanning

    def get_success_url(self):
        country = self.request.country
        return reverse('horizonscannings', kwargs={'country': country})


#Methods and Tools
class MethodsTools(BaseQuerysetView, ListView):

    model = models.MethodTool
    template_name = 'methodtool/methodstools.html'
    paginate_by = PER_PAGE


class MethodTool(BaseQuerysetView, DetailView):

    model = models.MethodTool
    template_name = 'methodtool/methodtool.html'


class MethodToolCreate(CreateView):

    model = models.MethodTool
    template_name = 'methodtool/methodtool_edit.html'
    form_class = forms.MethodToolForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(MethodToolCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('methodstools', kwargs={'country': country})
        return context


class MethodToolEdit(BaseQuerysetView, UpdateView):

    model = models.MethodTool
    template_name = 'methodtool/methodtool_edit.html'
    form_class = forms.MethodToolForm

    def get_context_data(self, *args, **kwargs):
        context = super(MethodToolEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class MethodToolDelete(BaseQuerysetView, DeleteView):

    model = models.MethodTool

    def get_success_url(self):
        country = self.request.country
        return reverse('methodstools', kwargs={'country': country})


#Uncertainties
class Uncertainties(BaseQuerysetView, ListView):

    model = models.Uncertainty
    template_name = 'uncertainty/uncertainties.html'
    paginate_by = PER_PAGE


class Uncertainty(BaseQuerysetView, DetailView):

    model = models.Uncertainty
    template_name = 'uncertainty/uncertainty.html'


class UncertaintyCreate(CreateView):

    model = models.Uncertainty
    template_name = 'uncertainty/uncertainty_edit.html'
    form_class = forms.UncertaintyForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(UncertaintyCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('uncertainties', kwargs={'country': country})
        return context


class UncertaintyEdit(BaseQuerysetView, UpdateView):

    model = models.Uncertainty
    template_name = 'uncertainty/uncertainty_edit.html'
    form_class = forms.UncertaintyForm

    def get_context_data(self, *args, **kwargs):
        context = super(UncertaintyEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class UncertaintyDelete(BaseQuerysetView, DeleteView):

    model = models.Uncertainty

    def get_success_url(self):
        country = self.request.country
        return reverse('uncertainties', kwargs={'country': country})


#Wild cards
class WildCards(BaseQuerysetView, ListView):

    model = models.WildCard
    template_name = 'wildcard/wildcards.html'
    paginate_by = PER_PAGE


class WildCard(BaseQuerysetView, DetailView):

    model = models.WildCard
    template_name = 'wildcard/wildcard.html'


class WildCardCreate(CreateView):

    model = models.WildCard
    template_name = 'wildcard/wildcard_edit.html'
    form_class = forms.WildCardForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(WildCardCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('wildcards', kwargs={'country': country})
        return context


class WildCardEdit(BaseQuerysetView, UpdateView):

    model = models.WildCard
    template_name = 'wildcard/wildcard_edit.html'
    form_class = forms.WildCardForm

    def get_context_data(self, *args, **kwargs):
        context = super(WildCardEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class WildCardDelete(BaseQuerysetView, DeleteView):

    model = models.WildCard

    def get_success_url(self):
        country = self.request.country
        return reverse('wildcards', kwargs={'country': country})


#Early warnings
class EarlyWarnings(BaseQuerysetView, ListView):

    model = models.EarlyWarning
    template_name = 'earlywarning/earlywarnings.html'
    paginate_by = PER_PAGE


class EarlyWarning(BaseQuerysetView, DetailView):

    model = models.EarlyWarning
    template_name = 'earlywarning/earlywarning.html'


class EarlyWarningCreate(CreateView):

    model = models.EarlyWarning
    template_name = 'earlywarning/earlywarning_edit.html'
    form_class = forms.EarlyWarningForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(EarlyWarningCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('earlywarnings', kwargs={'country': country})
        return context


class EarlyWarningEdit(BaseQuerysetView, UpdateView):

    model = models.EarlyWarning
    template_name = 'earlywarning/earlywarning_edit.html'
    form_class = forms.EarlyWarningForm

    def get_context_data(self, *args, **kwargs):
        context = super(EarlyWarningEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class EarlyWarningDelete(BaseQuerysetView, DeleteView):

    model = models.EarlyWarning

    def get_success_url(self):
        country = self.request.country
        return reverse('earlywarnings', kwargs={'country': country})


#Indicators
class Indicators(BaseQuerysetView, ListView):

    model = models.Indicator
    template_name = 'indicators/indicators.html'


class Indicator(BaseQuerysetView, DetailView):

    model = models.Indicator
    template_name = 'indicators/indicator.html'


class IndicatorCreate(CreateView):

    model = models.Indicator
    template_name = 'indicators/indicator_edit.html'
    form_class = forms.IndicatorForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(IndicatorCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('indicators', kwargs={'country': country})
        return context


class IndicatorEdit(BaseQuerysetView, UpdateView):

    model = models.Indicator
    template_name = 'indicators/indicator_edit.html'
    form_class = forms.IndicatorForm

    def get_context_data(self, *args, **kwargs):
        context = super(IndicatorEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class IndicatorDelete(BaseQuerysetView, DeleteView):

    model = models.Indicator

    def get_success_url(self):
        country = self.request.country
        return reverse('indicators', kwargs={'country': country})


#Trends
class Trends(BaseQuerysetView, ListView):

    model = models.Trend
    template_name = 'trends/trends.html'
    paginate_by = PER_PAGE


class Trend(BaseQuerysetView, DetailView):

    model = models.Trend
    template_name = 'trends/trend.html'


class TrendCreate(CreateView):

    model = models.Trend
    template_name = 'trends/trend_edit.html'
    form_class = forms.TrendForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(TrendCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('trends', kwargs={'country': country})
        return context


class TrendEdit(BaseQuerysetView, UpdateView):

    model = models.Trend
    template_name = 'trends/trend_edit.html'
    form_class = forms.TrendForm

    def get_context_data(self, *args, **kwargs):
        context = super(TrendEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TrendDelete(BaseQuerysetView, DeleteView):

    model = models.Trend

    def get_success_url(self):
        country = self.request.country
        return reverse('trends', kwargs={'country': country})


#BLOSSOM
class Blossoms(BaseQuerysetView, ListView):

    model = models.Blossom
    template_name = 'blossoms/blossoms.html'
    paginate_by = PER_PAGE


class Blossom(BaseQuerysetView, DetailView):

    model = models.Blossom
    template_name = 'blossoms/blossom.html'


class BlossomCreate(CreateView):

    model = models.Blossom
    template_name = 'blossoms/blossom_edit.html'
    form_class = forms.BlossomForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(BlossomCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('blossoms', kwargs={'country': country})
        return context


class BlossomEdit(BaseQuerysetView, UpdateView):

    model = models.Blossom
    template_name = 'blossoms/blossom_edit.html'
    form_class = forms.BlossomForm

    def get_context_data(self, *args, **kwargs):
        context = super(BlossomEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class BlossomDelete(BaseQuerysetView, DeleteView):

    model = models.Blossom

    def get_success_url(self):
        country = self.request.country
        return reverse('blossoms', kwargs={'country': country})


#Thematic category
class ThematicCategories(BaseQuerysetView, ListView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_categories.html'


class ThematicCategory(BaseQuerysetView, DetailView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category.html'

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(ThematicCategory, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('thematic_categories', kwargs={'country': country})
        return context


class ThematicCategoryCreate(CreateView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category_edit.html'
    form_class = forms.ThematicCategoryForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(ThematicCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('thematic_categories', kwargs={'country': country})
        return context


class ThematicCategoryEdit(BaseQuerysetView, UpdateView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category_edit.html'
    form_class = forms.ThematicCategoryForm

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class ThematicCategoryDelete(BaseQuerysetView, DeleteView):

    model = models.ThematicCategory

    def get_success_url(self):
        country = self.request.country
        return reverse('thematic_categories', kwargs={'country': country})


#Geographical Scale
class GeographicalScales(BaseQuerysetView, ListView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scales.html'


class GeographicalScale(BaseQuerysetView, DetailView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale.html'


class GeographicalScaleCreate(CreateView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale_edit.html'
    form_class = forms.GeographicalScaleForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(GeographicalScaleCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('geographical_scales', kwargs={'country': country})
        return context


class GeographicalScaleEdit(BaseQuerysetView, UpdateView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale_edit.html'
    form_class = forms.GeographicalScaleForm

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalScaleEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalScaleDelete(BaseQuerysetView, DeleteView):

    model = models.GeographicalScale

    def get_success_url(self):
        country = self.request.country
        return reverse('geographical_scales', kwargs={'country': country})


#Geographical Coverage
class GeographicalCoverages(BaseQuerysetView, ListView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverages.html'


class GeographicalCoverage(BaseQuerysetView, DetailView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage.html'


class GeographicalCoverageCreate(CreateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage_edit.html'
    form_class = forms.GeographicalCoverageForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(GeographicalCoverageCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('geographical_coverages', kwargs={'country': country})
        return context


class GeographicalCoverageEdit(BaseQuerysetView, UpdateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage_edit.html'
    form_class = forms.GeographicalCoverageForm

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalCoverageEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalCoverageDelete(BaseQuerysetView, DeleteView):

    model = models.GeographicalCoverage

    def get_success_url(self):
        country = self.request.country
        return reverse('geographical_coverages', kwargs={'country': country})


#Scenarios
class Scenarios(BaseQuerysetView, ListView):

    model = models.Scenario
    template_name = 'scenarios/scenarios.html'


class Scenario(BaseQuerysetView, DetailView):

    model = models.Scenario
    template_name = 'scenarios/scenario.html'


class ScenarioCreate(CreateView):

    model = models.Scenario
    template_name = 'scenarios/scenario_edit.html'
    form_class = forms.ScenarioForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(ScenarioCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('scenarios', kwargs={'country': country})
        return context


class ScenarioEdit(BaseQuerysetView, UpdateView):

    model = models.Scenario
    template_name = 'scenarios/scenario_edit.html'
    form_class = forms.ScenarioForm

    def get_context_data(self, *args, **kwargs):
        context = super(ScenarioEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class ScenarioDelete(BaseQuerysetView, DeleteView):

    model = models.Scenario

    def get_success_url(self):
        country = self.request.country
        return reverse('scenarios', kwargs={'country': country})


#Steep Category
class SteepCategories(BaseQuerysetView, ListView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_categories.html'


class SteepCategory(BaseQuerysetView, DetailView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category.html'


class SteepCategoryCreate(CreateView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category_edit.html'
    form_class = forms.SteepCategoryForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(SteepCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('steep_categories', kwargs={'country': country})
        return context


class SteepCategoryEdit(BaseQuerysetView, UpdateView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category_edit.html'
    form_class = forms.SteepCategoryForm

    def get_context_data(self, *args, **kwargs):
        context = super(SteepCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SteepCategoryDelete(BaseQuerysetView, DeleteView):

    model = models.SteepCategory

    def get_success_url(self):
        country = self.request.country
        return reverse('steep_categories', kwargs={'country': country})


#Timeline
class Timelines(BaseQuerysetView, ListView):

    model = models.Timeline
    template_name = 'timelines/timelines.html'


class Timeline(BaseQuerysetView, DetailView):

    model = models.Timeline
    template_name = 'timelines/timeline.html'


class TimelineCreate(CreateView):

    model = models.Timeline
    template_name = 'timelines/timeline_edit.html'
    form_class = forms.TimelineCreateForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(TimelineCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('timelines', kwargs={'country': country})
        return context


class TimelineEdit(BaseQuerysetView, UpdateView):

    model = models.Timeline
    template_name = 'timelines/timeline_edit.html'
    form_class = forms.TimelineCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(TimelineEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TimelineDelete(BaseQuerysetView, DeleteView):

    model = models.Timeline
    def get_success_url(self):
        country = self.request.country
        return reverse('timelines', kwargs={'country': country})
