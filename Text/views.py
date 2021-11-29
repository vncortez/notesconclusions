from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from NotesConclusions.rules import default_date_format
from Text.models import NodeText, TypeOfText
# Create your views here.


class TextViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeText
        fields = ['sub_titulo','text', 'data_criacao']
        
    data_criacao = serializers.DateTimeField(format=default_date_format())
    
    def to_representation(self, instance : NodeText):
        representation = super().to_representation(instance)
        
        representation.update({
            'titulos': instance.titulos.all().values('text', 'order', 'type_of'),
            'author': instance.author,
            'type_of': instance.type_of_text
        })
        
        
        return representation    



class TextViewSet(RetrieveAPIView):
    
    queryset = NodeText.objects.all()
    serializer_class = TextViewSerializer
    
    def retrieve(self, request, *args, **kwargs):
        usuario = request.user
        texts = NodeText.objects.filter(usuario=usuario)
        texts_serializer = TextViewSerializer(texts, many=True)
    
        return Response(data=texts_serializer.data)
    

text_viewset = TextViewSet.as_view()

# it could be become a static part or predefined
class TypesFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfText
        exclude = ['id']

class TypesFoundViewSet(RetrieveAPIView):
    queryset = TypeOfText.objects.all()
    serializer_class = TypesFoundSerializer
    permission_classes = [permissions.IsAuthenticated]
 
types_found_viewset = TypesFoundViewSet.as_view()