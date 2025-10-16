
## ********Day 55 Start**********

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


## ********Day 55 Start(Manual)**********

## Advanced Python Decorator Functions



def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

# Apply the decorator manually
create_blog_post = is_authenticated_decorator(create_blog_post)

# Create a user and test
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

new_user = User("Angela")
new_user.is_logged_in = True

create_blog_post(new_user)
