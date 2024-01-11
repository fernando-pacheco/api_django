from rest_framework import viewsets, generics, status
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer, AlunoSerializerV2
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""

    queryset = Aluno.objects.all()
    def get_serializer_class(self):
        if self.request.version =='v2':
            return AlunoSerializerV2
        return AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'path']

    
    def create(self, request):
        """Auto-documentação da view cursos"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'path'] # permissões dos verbos http 
    
    @method_decorator(cache_page(20))
    def dispatch(self,*args, **kwargs):
        return super(MatriculasViewSet, self).dispatch(*args, **kwargs)
    


class ListaMatriculasAluno(generics.ListAPIView):
    """Listar as matriculas de cada aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculaAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listar os alunos matriculados na curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosMatriculadosSerializer
