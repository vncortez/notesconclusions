from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from Text.models import NodeText, TypeOfText
# Create your views here.


class TextViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeText
        fields = ['sub_tutulo','text', 'data_criacao']
    
    def to_representation(self, instance : NodeText):
        representation = super().to_representation(instance)
        
        representation.update({
            'titulos': instance.titulos.all().values('text', 'order', 'type_of'),
            'author': instance.author,
            'type_of': instance.type_of_text
        })
        
        
        return representation    



class TextViewSet(viewsets.ModelViewSet):
    
    queryset = NodeText.objects.all()
    serializer_class = TextViewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# it could be become a static part or predefined
class TypesFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfText
        exclude = ['id']

class TypesFoundViewSet(viewsets.ModelViewSet):
    queryset = TypeOfText.objects.all()
    serializer_class = TypesFoundSerializer
    permission_classes = [permissions.IsAuthenticated]
 