from user import User
from post import Post

user_one = User("jure@gmail.com", "Jure", "pass", "DevOps Engineer")

user_one.get_user_info()
user_one.change_job_title("Cleaner")
user_one.get_user_info()

user_two = User("grega@gmail.com", "Grega", "pass1", "Q&A Engineer")

user_two.get_user_info()

new_post = Post("this is my message", user_two.name)
new_post.get_post_info()