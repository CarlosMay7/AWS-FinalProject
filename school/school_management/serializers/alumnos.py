from rest_framework import serializers

class AlumnoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    matricula = serializers.CharField()
    promedio = serializers.FloatField()

    def validate_nombres(self, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("El nombre es inválido.")
        return value

    def validate_apellidos(self, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("El apellido es inválido.")
        return value

    def validate_matricula(self, value):
        if not value or not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("La matrícula es inválida.")
        return value

    def validate_promedio(self, value):
        if not isinstance(value, (float, int)) or value < 0:
            raise serializers.ValidationError("El promedio debe ser numérico y mayor o igual a 0.")
        return value
