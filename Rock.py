class Players:
    rock = "1"
    paper = "2"
    scissor = "3"

    def __init__(self):
        self.name = input("Enter Your Name - ")

    def show(self):
        self.move()
        print("Player - ",self.name)
        print("Player",self.move)

    def move(self):
        x = input(print("Enter your move",self.name))
        self.move = x

    def compare(self,other):
        self.show()
        other.show()
        if self.move() == "1" and other.move == "1":
            print("Tied")
        elif self.move() == "1" and other.move == "3":
            print(self.name," Wins")
        elif self.move() == "1" and other.move == "2":
            print(other.name,"Wins")
        elif self.move() == "2" and other.move == "2":
            print("Tied")
        elif self.move() == "2" and other.move == "3":
            print(other.name, " Wins")
        elif self.move() == "2" and other.move == "1":
            print(self.name, "Wins")
        elif self.move() == "3" and other.move == "3":
            print("Tied")
        elif self.move() == "3" and other.move == "2":
            print(self.name, " Wins")
        elif self.move() == "3" and other.move == "1":
            print(other.name, "Wins")


print("*******ROCK PAPER SCISSOR********")
print(" For Rock Press 1")
print(" For Paper Press 2")
print(" For Scissor press 3")

player1 = Players()
player2 = Players()
player1.show()
player2.show()
player1.move()
player2.move()
player1.compare(player2)

i = int(input("Do you want to have another match ? \nIf Yes than Press 1"))
if i == 1:
    player1.move()
    player2.move()
    player1.compare(player2)
else:
    print('OK Bye')