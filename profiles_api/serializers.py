from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Seraliza un campo para probar nuestro APIView """
    name = serializers.CharField(max_length=10)