"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Update Test
"""

# System
from django.urls import reverse
from rest_framework.test import APITestCase

# Project
from core.constants import SYSTEM_CODE
from core.jwt import CustomJWTAuthentication
from app.users.models import User
from app.boards.models import Board


class UpdateTest(APITestCase):
    """
    게시글 수정 테스트
    """

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(email="test@test.com", password="password1234")
        cls.user_access_token = CustomJWTAuthentication.create_access_token(user=cls.user)
        cls.data = {
            "title": "Test Title_Update",
            "content": "Test Content_Update",
        }

    # 게시글 수정 성공
    def test_detail_board_success(self):
        board = Board.objects.create(title="Test Title", content="Test Content", author=self.user)

        url = reverse("api-boards:detail-update-delete-board", kwargs={"board_id": int(board.id)})

        response = self.client.put(
            path=url,
            HTTP_AUTHORIZATION=f"Bearer {self.user_access_token}",
            data=self.data,
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["code"], SYSTEM_CODE.SUCCESS[0])
