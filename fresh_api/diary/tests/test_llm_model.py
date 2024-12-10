# tests.py
import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, MagicMock
import torch

class TestAlphaInstruct(APITestCase):
    def setUp(self):
        self.url = reverse('alpha-instruct')
        self.valid_payload = {"input": "안녕 너한테 물어볼게있어"}
        self.invalid_payload = {}

    def test_invalid_request(self):
        print('유효하지 않는 응답')
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('transformers.AutoModelForCausalLM.from_pretrained')
    @patch('transformers.AutoTokenizer.from_pretrained')
    def test_valid_request(self, mock_tokenizer, mock_model):
        print('유효한 응답')
        # Mock 설정
        mock_device = torch.device('cpu')
        mock_model.return_value.device = mock_device
        
        # 실제 텐서 생성
        mock_input_tensor = torch.tensor([[1, 2, 3]])
        mock_output_tensor = torch.tensor([[4, 5, 6]])
        
        # Mock 응답 설정
        mock_tokenizer.return_value.apply_chat_template.return_value = mock_input_tensor
        mock_model.return_value.generate.return_value = mock_output_tensor
        mock_tokenizer.return_value.decode.return_value = "테스트 응답입니다."

        response = self.client.post(self.url, self.valid_payload, format='json')
        
        print(f'test Response >>>>>> {response.data}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.data)
        self.assertTrue(len(response.data['response']) > 0)

    # def test_real_model_response(self):
    #     print('모델응답 테스트')
    #     test_input = {"input": "테스트 질문입니다."}
    #     response = self.client.post(self.url, test_input, format='json')
        
    #     assert response.status_code == 200
    #     assert 'response' in response.data
    #     if 'response' in response.data:
    #         print(f"Response content: {response.data['response']}")  # 디버깅용
    #     assert isinstance(response.data['response'], str)