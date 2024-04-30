"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Create Test
"""

# System
from django.urls import reverse
from rest_framework.test import APITestCase

# Project
from core.constants import SYSTEM_CODE
from core.jwt import CustomJWTAuthentication
from app.users.models import User
from app.boards.models import Board


class CreateTest(APITestCase):
    """
    게시글 생성 테스트
    """

    url = reverse("api-boards:create-list-board")

    email = "test@test.com"
    password = "password1234"

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(email="test@test.com", password="password1234")
        cls.user_access_token = CustomJWTAuthentication.create_access_token(user=cls.user)
        cls.user_refresh_token = CustomJWTAuthentication.create_refresh_token(user=cls.user)
        cls.expired_token = CustomJWTAuthentication.create_test_token(user=cls.user)
        cls.data = {
            "title": "Test Title",
            "content": "Test Content",
        }

    # 게시글 생성 성공
    def test_create_board_success(self):
        response = self.client.post(
            path=self.url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_access_token}",
            data=self.data,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["code"], SYSTEM_CODE.SUCCESS[0])
