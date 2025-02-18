def greet(**kwargs):
    username = kwargs.get("username")
    is_loggedin = kwargs.get("is_loggedin")
    is_subscribed = kwargs.get("is_subscribed")

    if username is not None:
        print(username)

    if is_loggedin is not None:
        print(is_loggedin)

    if is_subscribed is not None:
        print(is_subscribed)

    print("==========================================")


greet()
greet(username="sakib")
greet(username="rakib", is_loggedin=True)
greet(username="rakib", is_loggedin=True, is_subscribed=False)
