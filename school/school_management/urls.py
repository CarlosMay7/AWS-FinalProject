from django.urls import path
from school_management.views.alumnos import AlumnosView, AlumnoDetailView
from school_management.views.profesores import ProfesoresView, ProfesorDetailView

urlpatterns = [
    path('alumnos', AlumnosView.as_view()),
    path('alumnos/<int:id>', AlumnoDetailView.as_view()),
    path('profesores', ProfesoresView.as_view()),
    path('profesores/<int:id>', ProfesorDetailView.as_view()),
]
