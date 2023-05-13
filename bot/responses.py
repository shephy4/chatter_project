from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
    "Hey :-)",
    "Hello, thanks for visiting our site",
    "Hi there, what can I do for you?",
    "Hi there, how can I help?")


        

class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
                "Expecting your order, thanks for checking us out",
                "Have a nice day",
                "Bye! Come back again soon.")

class ItemResponse(GenericRandomResponse):
    choices = ("We sell t-shirts, shorts/knickers, sweatshirts, hoodies, joggers, tote-bags, bucket hats, face caps.",
                "We have t-shirts, shorts/knickers, sweatshirts, hoodies, joggers, tote-bags, bucket hats, face caps.",
                "Kindly visit our site for the latest collection https://sylphhclothings.com/shop/",
                "This link would give you an idea of who we are https://sylphhclothing.com/?cms_block=about-brand")


class ThanksResponse(GenericRandomResponse):
    choices = ("Happy to help!", "Any time!", "My pleasure")


class PaymentResponse(GenericRandomResponse):
    choices = ("We accept VISA, Mastercard and Paypal",
          "We accept most major credit cards, and Paypal")

class DeliveryResponse(GenericRandomResponse):
    choices = ("Delivery takes 2-4 days",
          "Shipping takes 2-4 days")


class FunnyResponse(GenericRandomResponse):
    choices = ("Why did the hipster burn his mouth? He drank the coffee before it was cool.",
          "What did the buffalo say when his son left for college? Bison.")