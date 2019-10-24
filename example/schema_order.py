from graphene import ObjectType, String


class Order(ObjectType):
    orderId = String()
    dog = String()