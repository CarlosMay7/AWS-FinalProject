from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from school_management.serializers.alumnos import AlumnoSerializer
from school_management.data.alumnos import alumnos


class AlumnosView(APIView):
    def get(self, request):
        try:
            return Response(alumnos, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = AlumnoSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            alumno = serializer.validated_data

            if "id" not in alumno or alumno["id"] is None:
                alumno["id"] = len(alumnos) + 1

            alumnos.append(alumno)
            return Response(alumno, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        return Response({"error": "Método no permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AlumnoDetailView(APIView):
    def get_alumno(self, id):
        for alumno in alumnos:
            if alumno["id"] == id:
                return alumno
        return None

    def get(self, request, id):
        try:
            alumno = self.get_alumno(id)
            if not alumno:
                return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            return Response(alumno, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            alumno = self.get_alumno(id)
            if not alumno:
                return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            serializer = AlumnoSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            alumno.update(serializer.validated_data)
            return Response(alumno, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            alumno = self.get_alumno(id)
            if not alumno:
                return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            alumnos.remove(alumno)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
