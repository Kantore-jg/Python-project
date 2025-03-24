class User:
    def __init__(self ,user_id ,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0

    def follower(self, user):
        user.followers+=1
        self.following+=1


User_1 = User("001","Kantore")
User_2 = User("002", "Lee")

User_2.follower(User_1)
print(User_1.followers)
print(User_1.following)
print(User_2.followers)
print(User_2.following)
# User_1.id="001"
# User_1.username="Kantore"
#print(User_1.id)
