from rest_framework import serializers
from apps.login.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
    def to_representation(self,instance):
        print(instance)
        return {
            'id_usuario': instance['id'],
            'Nombre_usuario': instance['username'],
            'Correo_usuario': instance['email'],
            'Contrasenha_usuario' : instance['password']
        }
        
         
### Este fue un ejemplo
        
# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     email = serializers.EmailField()
#     #Validacion nombre
#     def validate_name(self,value):
#         if 'JohanSabogalCanoas' in value:
#             raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre ')
        
#         return value
    
#     def validate_email(self,value):
#         if value == '':
#             raise serializers.ValidationError('Error, el campo correo no puede ser vacio')
#         return value
    
#     def validate(self, data):
#         return data
    
#     def create(self, validate_data): 
#         return User.objects.create(**validate_data)
        
#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name',instance.name)
#         instance.email = validate_data.get('email',instance.email)
#         instance.save()
#         return instance