from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from school_management.serializers.profesores import ProfesorSerializer
from school_management.data.profesores import profesores

class ProfesoresView(APIView):
    def get(self, request):
        try:
            return Response(profesores, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ProfesorSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            profesor = serializer.validated_data

            if "id" not in profesor or profesor["id"] is None:
                profesor["id"] = len(profesores) + 1

            profesores.append(profesor)
            return Response(profesor, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        return Response({"error": "Método no permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ProfesorDetailView(APIView):
    def get_profesor(self, id):
        for profesor in profesores:
            if profesor["id"] == id:
                return profesor
        return None

    def get(self, request, id):
        try:
            profesor = self.get_profesor(id)
            if not profesor:
                return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            return Response(profesor, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            profesor = self.get_profesor(id)
            if not profesor:
                return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            serializer = ProfesorSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            profesor.update(serializer.validated_data)
            return Response(profesor, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            profesor = self.get_profesor(id)
            if not profesor:
                return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            profesores.remove(profesor)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
