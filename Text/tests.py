from django.test import TestCase
from NotesConclusions.rules import default_date_format

from Text.factory import NodeTextFactory, UsuarioFactory
from django.urls import reverse
from rest_framework import status
from datetime import datetime
# Create your tests here.




class TextViewSetTest(TestCase):
    
    def setUp(self) -> None:
        self.usuario = UsuarioFactory(username='MeuUsuario')
        self.client.force_login(self.usuario)
        self.texts = NodeTextFactory(usuario=self.usuario)
    
    
    def test_get_success(self):
        response = self.client.get(reverse('api_text'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data_criacao = datetime.strftime(self.texts.data_criacao, default_date_format())
        self.assertEqual(response.json(),
                         [{
                             'sub_titulo': 'Minha primeira matéria',
                             'text': 'Meu texto bem bonito',
                             'data_criacao': data_criacao,
                             'titulos': [{
                                 'text': 'Algum titulo', 'order': 1, 'type_of': '#'
                                 }], 
                             'author': self.usuario.username, 
                             'type_of': 'plaintext'
                        }])
        