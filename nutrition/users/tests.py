from django.test import TestCase, RequestFactory, Client
from users.models import *
from users.views import *
#Create your tests here.

class NutriuserTestCase(TestCase):
    def setUp(self):
        print('in setup in order to create user for test')
        self.factory = RequestFactory()
        self.titi = Nutriuser.objects.create(username='titi', password='meknes', height=100, weight=100, birthdate='2017-02-01', gender='m')
        self.toti=Nutriuser.objects.create(username='toti', password='meknes', height=100, weight=100, birthdate='2017-02-01', gender='m')

    #TEST DATABASE TRANSACTION
    def test_user_pk(self):
        self.assertEqual(self.titi.pk, 1)
        self.assertEqual(self.toti.pk, 2)

    def test_details(self):
        request = self.factory.get('/api/users')
        #response = NutriuserViewset.as_view()(request)
        #self.assertEqual(response.status_code, 200)
        resp = self.client.get('/api/users')
        self.assertEqual(resp.status_code, 301) #redirect first then code 200

    def test_client(self):
        c = Client()
        # reponse = c.get('/admin')
        # c.login(username='otman', password='meknes8231')
        # self.assertEqual(reponse.status_code, 301) #receive login page
        reponse = c.post('/admin/login/?next=/admin', {"username": 'otman', 'password': 'meknes8231'})
        self.assertEqual(reponse.status_code, 200)

    def test_create_user(self):
        # !! ALL USER MUST BE CREATED IN SETUP FUNCTION
        #Nutriuser.objects.create(username='titi', password='meknes', height=100, weight=100, birthdate='2017-02-01', gender='m')
        pass

    def test_get_user_created(self):
        #queryset = Nutriuser.objects.all()
        #print('my queryst in getusercreated',queryset)
        titi = Nutriuser.objects.get(username='titi')
        print('my user in get user created ',titi)
        #self.assertEqual(user, ['titi','toti'])
        self.assertEqual(titi.username, 'titi')

    def test_update_user(self):
        user = Nutriuser.objects.get(username='titi')
        print('my update user behind', user.username)
        user.username = 'tata'
        print('my update user after', user.username)
        self.assertEqual(user.username, 'tata')
