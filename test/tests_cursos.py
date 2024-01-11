from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso Teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso Teste 2', nivel='I'
        )
        self.curso_3 = Curso.objects.create(
            codigo_curso='CTT3', descricao='Curso Teste 3', nivel='A'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar se a listagem de cursos funciona"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar se o cadastro de um novo curso funciona"""
        data = {
            'codigo_curso': 'CTT4',
            'descricao': 'Curso Teste 4',
            'nivel': 'B'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_excluir_curso(self):
        """Teste para verificar se a requisição DELETE não é permitida para Cursos"""
        url = reverse('Cursos-detail', args=[self.curso_1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_requisicao_put_para_alterar_curso(self):
        """Teste para verificar se a atualização de um curso funciona"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1 Atualizado',
            'nivel': 'I'
        }
        url = reverse('Cursos-detail', args=[self.curso_1.id])
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    