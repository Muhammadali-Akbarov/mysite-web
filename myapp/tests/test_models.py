from django.test import TestCase

from myapp.models import MyBots
from myapp.models import Comments
from myapp.models import MyResume
from myapp.models import MyYouTube
from myapp.models import GetInTouch
from myapp.models import MyProjects
from myapp.models import ProjectCategory



class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        self.comment = Comments.objects.create(
            name="Muhammadali",
            comment="Lorem Ipsum is simply dummy text",
        )
        self.proj_cat = ProjectCategory.objects.create(
            name="BillingSystems"
        )
        self.my_proj = MyProjects.objects.create(
            category=self.proj_cat,
            side="left",
            image="static/images/intro.jpg",
            body="Lorem Ipsum is simply dummy text",
            link="http://www.my-project.com/imagesLoaded"
        )
        self.my_bot = MyBots.objects.create(
            category=self.proj_cat,
            name="ABC WikiBot",
            image="static/images/abc_wiki.png",
            link="http://t.me/@abc_wiki",
            file="media/videos/abc-wikibot_FHHhEoP.mp4"
        )
        self.get_in_touch = GetInTouch.objects.create(
            fullname="Muhammadali Akbarov",
            email="muhammadali.akbarov@gmail.com",
            body="Lorem Ipsum is simply dummy text"
        )
        self.my_youtube = MyYouTube.objects.create(
            file="media/videos/Paycom.mp4",
        )
        
    def test_comments_instance(self) -> None:
        """Checks comments created in database."""
        comment = Comments.objects.get(name="Muhammadali")
        self.assertEqual(comment.name, "Muhammadali")
        self.assertEqual(comment.imageURL,'/media/profile/default.jpeg')
        self.assertEqual(comment.comment, 'Lorem Ipsum is simply dummy text')

    def test_my_resume_instance(self) -> None:
        """Checks my resume instance in database."""
        _file = MyResume.objects.create(file='static/resume.pdf')
        self.assertEquals(bool(_file), True)
    
    def test_project_instance(self) -> None:
        """Checks project instance in database."""
        category = ProjectCategory.objects.get(name='BillingSystems')
        self.assertEquals(category.name, 'BillingSystems')
    
    def test_my_project_instance(self) -> None:
        """Checks my projects instance in database."""
        my_proj = MyProjects.objects.get(
            category=self.proj_cat, side="left", link="http://www.my-project.com/imagesLoaded"
        )
        self.assertEquals(my_proj.image, 'static/images/intro.jpg')
        self.assertEquals(my_proj.body, 'Lorem Ipsum is simply dummy text')
    
    def test_my_bots_instance(self) -> None:
        """Checks my bots instance in database."""
        my_bot = MyBots.objects.get(
            category=self.proj_cat,
            name="ABC WikiBot",
        )
        self.assertEquals(my_bot.image, 'static/images/abc_wiki.png')
        self.assertEquals(my_bot.link, 'http://t.me/@abc_wiki')
        self.assertEquals(my_bot.file, 'media/videos/abc-wikibot_FHHhEoP.mp4')
        
    def test_get_in_touch_instance(self) -> None:
        """Checks my touch instance in database."""
        ticket = GetInTouch.objects.get(
            email="muhammadali.akbarov@gmail.com"
        )
        self.assertEquals(ticket.fullname, 'Muhammadali Akbarov')
        self.assertEquals(ticket.body, 'Lorem Ipsum is simply dummy text')
    
    def test_my_youtube_instance(self) -> None:
        """Checks my youtube instance in database."""
        my_youtube = MyYouTube.objects.get(file="media/videos/Paycom.mp4")
        self.assertEquals(bool(my_youtube), True)
    