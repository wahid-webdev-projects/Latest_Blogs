from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

# Creclassmethod re.

class PostTestCase(TestCase):
    @classmethod 
    def setUpTestData(cls):
        cls.user=User.objects.create_user(
            username="user", password="secret", email="user@example.com"
        )

        cls.post=Post.objects.create(
            title="A test title",
            body="A test body",
            author=cls.user
        )
    def test_post_model(self):
        self.assertEqual(self.post.title, "A test title")
        self.assertEqual(self.post.body, "A test body")
        self.assertEqual(self.post.author.username, "user")
        self.assertEqual(self.post.__str__(), "A test title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
    def test_url_exists_at_correct_location_listview(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_exists_at_correct_location_detailview(self): # new
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)
    def test_post_listview(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A test body")
        self.assertTemplateUsed(response, "home.html")
    def test_post_detailview(self): # new
        response = self.client.get(reverse("post_detail",
        kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A test title")
        self.assertTemplateUsed(response, "post_detail.html")

