from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializer

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from product.models import Product


class GetSellerProductViewTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)

    def test_get_seller_product_success(self):
        url = '/api/mymodel/'
        data = {'field1': 'value1', 'field2': 'value2'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class GetSellerProductViewTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username="seller")
#         self.product1 = Product.objects.create(
#             name="Product 1", description="description1", price=890, seller=self.user
#         )
#         self.product2 = Product.objects.create(
#             name="Product 2", description="description1", price=890, seller=self.user
#         )

#     def test_get_seller_product_success(self):
#         response = self.client.get(
#             reverse("getsellerproduct", kwargs={"user_id": self.user.id})
#         )
#         self.assertEqual(response.status_code, 200)
        # self.assertJSONEqual(
        #     response.content,
        #     ProductSerializer([self.product1, self.product2], many=True).data,
        # )

    # def test_get_seller_product_user_not_found(self):
    #     response = self.client.get(reverse("getsellerproduct", kwargs={"user_id": 999}))
    #     self.assertEqual(response.status_code, 404)

    # def test_get_seller_product_no_products(self):
    #     other_user = User.objects.create(username="other_seller")
    #     response = self.client.get(
    #         reverse("getsellerproduct", kwargs={"user_id": other_user.id})
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.content, b"[]"
    #     )  # Empty list returned when no products found
