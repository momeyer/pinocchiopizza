from django.test import TestCase, Client
from .models import Pizza, Order, OrderItem, OrderStatus, User, PizzaBaseType, PizzaTopping, Size, Sub, Salad, DinnerPlate, Pasta, Extra


class OrderTestCase(TestCase):

    def setUp(self):
        pending = OrderStatus.objects.create(order_status="PENDING")
        preparing = OrderStatus.objects.create(order_status="PREPARING")
        
        small = Size.objects.create(size='small')
        large = Size.objects.create(size="large")

        self.user = User.objects.create_user(
            username="user1", email="user1@user", password="user123")
        self.order = Order.objects.create(user=self.user, order_status=pending)
        BaseTypeRegular = PizzaBaseType.objects.create(base="Regular")
        BaseTypeSicilian = PizzaBaseType.objects.create(base="Sicilian")

        cheese = PizzaTopping.objects.create(topping="Cheese")
        one = PizzaTopping.objects.create(topping="One topping")
        two = PizzaTopping.objects.create(topping="Two toppings")
        three = PizzaTopping.objects.create(topping="Three toppings")
        special = PizzaTopping.objects.create(topping="Special")

        sicilianBase = PizzaBaseType.objects.get(base="Sicilian")
        regularBase = PizzaBaseType.objects.get(base="Regular")

        pizzaSicilian = Pizza.objects.create(
            base=sicilianBase, toppings=special, small=30.0, large=40.0)
        pizzaRegular = Pizza.objects.create(
            base=regularBase, toppings=special, small=20.0, large=30.0)

        order_item = OrderItem.objects.create(quantity=2, order=self.order, content_object=pizzaSicilian, object_id=pizzaSicilian.id, price=pizzaSicilian.small, size=small)

        sub = Sub.objects.create(
            ingredients="Meatballs", small=6.00, large=9.00)

        extra = Extra.objects.create(extra="garlic", price=0.50)

        pasta = Pasta.objects.create(ingredients="Baked Zitti", price=6.50)

        salad = Salad.objects.create(ingredients="garden salad", price=5.50)

        dinner = DinnerPlate.objects.create(
            ingredients="antipasto", small=40.00, large=60.00)

        self.client = Client()

    def test_order_count(self):
        count = Order.objects.count()
        self.assertEqual(1, count)

    def test_index(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["bases"].count(), 2)
        self.assertEqual(response.context["sizes"].count(), 2)
        self.assertEqual(response.context["toppingOptions"].count(), 5)
        self.assertEqual(response.context["sicilians"].count(), 1)
        self.assertEqual(response.context["regulars"].count(), 1)

    def test_login(self):
        response = self.client.post(
            '/login/', {'username': 'user1', 'password': 'user123'})
        self.assertEqual(response.context["user"], self.user)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_orderPizza(self):
        self.client.login(username='user1', password='user123')
        response = self.client.post(
            '/pizza/', {"sicilian_toppings": "Special", "size": 'small', "num": 3})
        items = OrderItem.objects.filter(order=self.order)
        self.assertEqual(items.count(), 2)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            '/pizza/', {"regular_toppings": "Special", "size": 'large', "num": 1})
        self.assertEqual(items.count(), 3)
        self.assertEqual(response.status_code, 200)

    def test_orderSub(self):
        self.client.login(username='user1', password='user123')
        response = self.client.post(
            '/Sub/', {"sub": "Meatballs", "size": 'small', "num": 1, "extra": "none"})
        items = OrderItem.objects.filter(order=self.order)
        self.assertEqual(items.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_orderPasta(self):
        self.client.login(username='user1', password='user123')
        response = self.client.post(
            '/Pasta/', {"pasta": "Baked Zitti", "num": 1})
        items = OrderItem.objects.filter(order=self.order)
        self.assertEqual(items.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_orderSalad(self):
        self.client.login(username='user1', password='user123')
        response = self.client.post(
            '/Salad/', {"salad": "garden salad", "num": 1})
        items = OrderItem.objects.filter(order=self.order)
        self.assertEqual(items.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_orderDinner(self):
        self.client.login(username='user1', password='user123')
        response = self.client.post(
            '/Dinner/', {"dinner": "antipasto", "size": "large", "num": 1})
        items = OrderItem.objects.filter(order=self.order)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(items.count(), 2)

    def test_removeItem(self):
        self.client.login(username='user1', password='user123')
        response = self.client.post('/Remove/', {"itemId": 1})
        items = OrderItem.objects.filter(order=self.order)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(items.count(), 0)

    def test_registerUser(self):
        response = self.client.post('/register/', {
                                                    "username": "John",
                                                    "password": "John111",
                                                    "fname": "John",
                                                    "lname": "Smith",
                                                    "email": "John@Smith",
                                                    "address": "street111",
                                                    "city": "cityaa",
                                                    "zipCode": 123,
                                                    "state": "state",
                                                    })
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        self.client.post('/register/', {
                                                    "username": "John",
                                                    "password": "John111",
                                                    "fname": "John",
                                                    "lname": "Smith",
                                                    "email": "John@Smith",
                                                    "address": "street111",
                                                    "city": "cityaa",
                                                    "zipCode": 123,
                                                    "state": "state",
                                                    })
        self.client.post('/Sub/', {"sub": "Meatballs", "size": 'small', "num": 1, "extra": "none"})
        # testig empty form (using information from db as address)
        response = self.client.post('/Checkout/', { "street": "",
                                                    "city": "",
                                                    "zip": "",
                                                    "state": "",
                                                    })
        self.assertEqual(response.status_code, 200)
        # testig filled form (updating db information)
        self.client.post('/login/', {'username': 'user1', 'password': 'user123'})
        response = self.client.post('/Checkout/',{ 
                                                    "street": "AnotherStreet",
                                                    "city": "AnotherCity",
                                                    "zip": 456,
                                                    "state": "AnotherState",
                                                 })
        self.assertEqual(response.status_code, 200)
        