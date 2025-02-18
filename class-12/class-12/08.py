# **kwargs


def greet(**kwargs):
    print(kwargs, type(kwargs))


greet()
greet(username="sakib")
greet(username="rakib", is_loggedin=True)
greet(username="rakib", is_loggedin=True, is_subscribed=False)
