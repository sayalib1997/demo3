from django.core.urlresolvers import reverse
from django.test.utils import override_settings

from flip.models import PhasesOfPolicy

from .base import BaseWebTest
from .base import PhasesOfPolicyFactory


@override_settings(SKIP_EDIT_AUTH=True, FRAME_URL=None)
class SettingsPolicyTests(BaseWebTest):

    def test_policy_new(self):
        data = PhasesOfPolicyFactory.attributes()
        url = reverse('settings:phases_of_policy_edit')
        resp = self.app.get(url)
        form = resp.forms['policy-form']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertObjectInDatabase(PhasesOfPolicy, title=data['title'])

    def test_policy_edit(self):
        policy = PhasesOfPolicyFactory()
        data = PhasesOfPolicyFactory.attributes()
        data['title'] = 'new title'
        url = reverse('settings:phases_of_policy_edit',
                      kwargs={'pk': policy.pk})
        resp = self.app.get(url)
        form = resp.forms['policy-form']
        self.populate_fields(form, self.normalize_data(data))
        form.submit().follow()
        self.assertEqual(1, PhasesOfPolicy.objects.count())
        self.assertObjectInDatabase(PhasesOfPolicy, title=data['title'])

    def test_policy_delete_confirm(self):
        policy = PhasesOfPolicyFactory()
        url = reverse('settings:phases_of_policy_delete',
                      kwargs={'pk': policy.pk})
        resp = self.app.get(url)
        self.assertEqual(200, resp.status_int)
        self.assertIn('settings/policy_confirm_delete.html',
                      resp.templates[0].name)

    def test_policy_delete(self):
        policy = PhasesOfPolicyFactory()
        url = reverse('settings:phases_of_policy_delete',
                      kwargs={'pk': policy.pk})
        resp = self.app.delete(url)
        self.assertEqual(302, resp.status_int)
        self.assertEqual(0, PhasesOfPolicy.objects.count())
