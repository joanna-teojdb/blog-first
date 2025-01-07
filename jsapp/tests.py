from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import Category, Post
from .forms import Postform
from .views import about, post_create

# Create your tests here.

class PostFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Testowa kategoria")

    def test_valid_form(self):
        form_data = {"title":"Poprawny tytul", 
                     "content":"Przykladowa tresc", 
                     "category":self.category.id}
        form = Postform(data=form_data)
        self.assertTrue(form.is_valid())

    def test_valid_form(self):
        form = Postform(data={})
        self.assertFalse(form.is_valid())

    # def test_clean_title(self):
    #     form_data = {"title":"Poprawny tytul", 
    #                  "content":"Przykladowa tresc", 
    #                  "category":self.category.id}
    #     form = Postform(data=form_data) 
    #     self.assertEqual(form.clean_title(), "Poprawny tytul")


class TestUrls(TestCase):
    def setUp(self):
        self.about_url = reverse('about')
        self.post_create_url = reverse('post_create')
        # print(reverse('about')) # sciezka do about
        # print(resolve(self.about_url)) # ResolverMatch obiekt

    def test_about_url(self):
        self.assertEqual(resolve(self.about_url).func, about)

    def test_post_create_url(self):
        self.assertEqual(resolve(self.post_create_url).func, post_create)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.about_url = reverse('about')
        self.post_create_url = reverse('post_create')
        # print(reverse('post_create')) # /post/new

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jsapp/about.html')

    def test_post_create_GET(self):
        response = self.client.get(self.post_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jsapp/post_form.html')


class TestModels(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Testowa kategoria")
        self.post = Post.objects.create(title="Testowy tytul", 
                     content="Przykladowa tresc", 
                     category=self.category)

    def test_post1(self):
        self.assertEqual(self.post.category.name, "Testowa kategoria")

    def test_post1(self):
        self.assertEqual(self.post.title, "Testowy tytul")