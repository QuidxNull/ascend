from class_user import User
from post import Post

app_user_one = User("quid@nn.com", "Johnny Quid", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "Reishma Kistow", "secret", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()