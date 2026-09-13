from django.test import TestCase
from django.urls import reverse

from .models import RSVPResponse, Wish


class WeddingViewTests(TestCase):
    def test_homepage_has_invitation_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Нұрсұлтан және Айдана')
        self.assertContains(response, '18.10.2026')

    def test_rsvp_list_page_is_accessible(self):
        response = self.client.get(reverse('responses'))
        self.assertEqual(response.status_code, 200)

    def test_rsvp_submission_is_saved_and_shown_in_list(self):
        response = self.client.post(reverse('home'), {
            'full_name': 'Айгерім Сейітова',
            'attendance': 'yes',
        })

        self.assertRedirects(response, f"{reverse('home')}?sent=rsvp#rsvp")
        self.assertTrue(RSVPResponse.objects.filter(full_name='Айгерім Сейітова').exists())
        response = self.client.get(reverse('responses'))
        self.assertContains(response, 'Айгерім Сейітова')

    def test_wish_submission_is_saved(self):
        response = self.client.post(reverse('home'), {
            'form_type': 'wish',
            'name': 'Данияр',
            'message': 'Бақыттарыңыз баянды болсын!',
        })

        self.assertRedirects(response, f"{reverse('home')}?sent=wish#wishes")
        self.assertTrue(Wish.objects.filter(name='Данияр').exists())
