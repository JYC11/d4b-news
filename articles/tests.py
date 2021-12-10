from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Article

# Create your tests here.


class NewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.article = Article.objects.create(
            title='Exciting news!!',
            body='wow so exciting!!!!!',
            author=self.user
        )
        self.client.login(username='testuser',password='secret') #just needed to add this???

    def test_string_representation(self):
        article = Article(title='Exciting news!!')
        self.assertEqual(str(article), article.title)

    def test_article_body(self):
        self.assertEqual(f'{self.article.title}', 'Exciting news!!')
        self.assertEqual(f'{self.article.body}', 'wow so exciting!!!!!')
        self.assertEqual(f'{self.article.author}', 'testuser')

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A Newspaper website built with Django.')
        self.assertTemplateUsed(response, 'home.html')

    def test_article_detail_view(self):
        response = self.client.get('/articles/1/')
        no_response = self.client.get('/article/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Exciting news!!')
        self.assertTemplateUsed(response, 'article_detail.html')

    def test_article_create(self):
        response = self.client.post(reverse('article_new'), {
            'title': 'New Title',
            'body': 'new text',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, 'New Title')
        self.assertEqual(Article.objects.last().body, 'new text')

    def test_article_update(self):
        response = self.client.post(reverse('article_edit', args='1'), {
            'title': 'New Title updated',
            'body': 'new text updated',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)

    def test_article_delete(self):
        response = self.client.post(reverse('article_delete', args='1'))
        self.assertEqual(response.status_code, 302)
