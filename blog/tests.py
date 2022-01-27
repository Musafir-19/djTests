from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post


User = get_user_model()
class BlogTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username = 'admin',
            email = 'admin@mail.ru',
            password = 'secret_key'
        )    

        self.post = Post.objects.create(
            title = 'Java',
            author = self.user,
            body = 'Java is good'
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Java')
        self.assertEqual(f'{self.post.author}', 'admin')
        self.assertEqual(f'{self.post.body}', 'Java is good')

    def test_post_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')