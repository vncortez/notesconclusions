from django.contrib.auth import get_user_model
import factory

from Text.models import NodeText, Title, TypeOfText


class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()


class TitleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Title
    
    order = 1
    text = 'Algum titulo'
    type_of = Title.TypeOf.a

class TypeOfTextFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TypeOfText
    
    text = 'plaintext'

class NodeTextFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NodeText

    text = 'Meu texto bem bonito'
    usuario = factory.SubFactory(UsuarioFactory)
    tipo_texto = factory.SubFactory(TypeOfTextFactory)
    
    sub_titulo = 'Minha primeira matéria'
    
        
    @factory.post_generation
    def titulos(self, created, extrated):
        if not created:
            return
        elif extrated:
            for titulo in extrated:
                self.titulos.add(titulo)
        else:
            return self.titulos.add(TitleFactory())
        
    
    
