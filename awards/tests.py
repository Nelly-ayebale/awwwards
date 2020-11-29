from django.test import TestCase
from .models import Profile,Project,Rating

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Afri',password='frog123')
        self.user.save()

        self.profile = Profile(user='Afri',name='Afri',bio='I love my continent',contact='0798765432')
        self.profile.save()

        def test_instance(self):
            self.assertTrue(isinstance(self.profile,Profile))

        def test_save_profile(self):
            self.profile.save_profile()
        
        def test_delete_user(self):
            self.profile.delete_profile()

class ProjectTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Afri',password='frog123')
        self.user.save()
        self.profile = Profile(user='Afri',name='Afri',bio='I love my continent',contact='0798765432')
        self.profile.save()

        self.project = Project(id=1,profile=self.user,title='Github Search',description='An application using github API',project_link='https://githubsearch.github.io')
        self.project.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

    def test_save_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)< 1)
    
    def test_all_projects(self):
        self.project.save_project()
        projects = Project.all_projects()
        self.assertTrue(len(projects)> 0)

    def test_search_by_title(self):
        self.project.save_project()
        projects = Project.search_by_title('Github Search')
        self.assertTrue(len(projects) > 0)
