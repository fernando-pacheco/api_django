from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status


class AlunoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.aluno_1 = Aluno.objects.create(
            nome='1', rg='1', cpf='1', data_nascimento='2000-01-01'
        )
        self.aluno_2 = Aluno.objects.create(
            nome='2', rg='2', cpf='2', data_nascimento='2000-01-01'
        )
        self.aluno_3 = Aluno.objects.create(
            nome='3', rg='3', cpf='3', data_nascimento='2000-01-01'
        )

    def test_requisicao_get_para_listar_alunos(self):
        """Teste para verificar se a listagem de alunos funciona"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_aluno(self):
        """Teste para verificar se o cadastro de um novo aluno funciona"""
        data = {
            'nome': '4',
            'rg': '4',
            'cpf': '4',
            'data_nascimento': '2000-01-01'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_alterar_aluno(self):
        """Teste para verificar se a atualização de um aluno funciona"""
        data = {
            'nome': '4',
            'rg': '4',
            'cpf': '4',
            'data_nascimento': '2000-01-01'
        }
        url = reverse('Alunos-detail', args=[self.aluno_1.id])
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_excluir_aluno(self):
        """Teste para verificar se a remoção de um aluno é permitida"""
        url = reverse('Alunos-detail', args=[self.aluno_1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)