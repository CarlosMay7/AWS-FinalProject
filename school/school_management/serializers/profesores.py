from rest_framework import serializers

class ProfesorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    numeroEmpleado = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    horasClase = serializers.IntegerField()

    def validate_numeroEmpleado(self, value):
        if not isinstance(value, int) or value <= 0:
            raise serializers.ValidationError("El número de empleado debe ser un entero positivo.")
        return value

    def validate_nombres(self, value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value

    def validate_apellidos(self, value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("El apellido no puede estar vacío.")
        return value

    def validate_horasClase(self, value):
        if not isinstance(value, int) or value < 0:
            raise serializers.ValidationError("La cantidad de horas debe ser un número positivo.")
        return value
