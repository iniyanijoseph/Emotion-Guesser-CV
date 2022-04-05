from fer import FER
import matplotlib.pyplot as plt 
import cv2
from tkinter import *
from PIL import Image, ImageTk
import random

window = Tk()
window.resizable(False, False)
window.title("KEWEM")
stream = cv2.VideoCapture(0)

hq = ["Never give up, for that is just the place and time that the tide will turn.– Harriet Beecher Stowe", "We must embrace pain and burn it as fuel for our journey. – Kenji Miyazawa", "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover. – Mark Twain", "Discouragement and failure are two of the surest stepping stones to success. – Dale Carnegie", "Do not let what you cannot do interfere with what you can do. – John Wooden", "Nothing splendid has ever been achieved except by those who dared believe that something inside of them was superior to circumstance. – Bruce Barton", "Be thankful for what you have and you’ll end up having more. If you concentrate on what you don’t have, you will never, ever have enough. – Oprah Winfrey", "Life is a series of natural and spontaneous changes. Don’t resist them – that only creates sorrow. Let reality be reality. Let things flow naturally forward in whatever way they like. – Lao Tzu", "A successful man is one who can lay a firm foundation with the bricks others have thrown at him. – David Brinkley"]
mhq = ["Focus on the journey, not the destination. Joy is found not in finishing an activity but in doing it. – Greg Anderson",  "When we stop opposing reality, action becomes simple, fluid, kind, and fearless. – Byron Katie", "Each morning when I open my eyes I say to myself: I, not events, have the power to make me happy or unhappy today. I can choose which it shall be. Yesterday is dead, tomorrow hasn’t arrived yet. I have just one day, today, and I’m going to be happy. – Groucho Marx", "Happiness resides not in possessions and not in gold, the feeling of happiness dwells in the soul. – Democritus", "If there is no struggle, there is no progress. – Frederick Douglass", "In essence, if we want to direct our lives, we must take control of our consistent actions. It’s not what we do once in a while that shapes our lives, but what we do consistently. – Tony Robbins", "A ship is always safe at the shore – but that is NOT what it is built for. – Albert Einstein", "The best way to cheer yourself up is to try to cheer somebody else up. – Mark Twain", "I believe that one defines oneself by reinvention. To not be like your parents. To not be like your friends. To be yourself. To cut yourself out of stone. – Henry Rollins", "Cherish your visions and your dreams as they are the children of your soul, the blueprints of your ultimate achievements. – Napoleon Hill"]
msq = ["Your destiny is to fulfill those things upon which you focus most intently. So choose to keep your focus on that which is truly magnificent, beautiful, uplifting and joyful. Your life is always moving toward something. – Ralph Marston", "Rise above the storm and you will find the sunshine. – Mario Fernandez", "Count your age by friends, not years. Count your life by smiles, not tears. – John Lennon", "Every small positive change we make in ourselves repays us in confidence in the future. – Alice Walker", "Life is like riding a bicycle. To keep your balance you must keep moving. – Albert Einstein", "The best way out is always through. – Robert Frost", "Your destiny is to fulfill those things upon which you focus most intently. So choose to keep your focus on that which is truly magnificent, beautiful, uplifting and joyful. Your life is always moving toward something. – Ralph Marston", "It does not matter how slowly you go as long as you do not stop. – Confucius", "Life has no limitations, except the ones you make. – Les Brown", "Don’t wait. The time will never be just right. – Napoleon Hill" ]
sq = [ "We are each gifted in a unique and important way. It is our privilege and our adventure to discover our own special light. – Mary Dunbar", "I have missed more than 9000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life. And that is why I succeed. – Michael Jordan", "If I persist long enough I will win. – Og Mandino", "With all its sham, drudgery, and broken dreams, it is still a beautiful world. Be cheerful. Strive to be happy. – Max Ehrmann", "Many men go fishing all of their lives without knowing that it is not fish they are after. – Henry David Thoreau", "It always seems impossible until it’s done. – Nelson Mandela", "Thankfully, persistence is a great substitute for talent. – Steve Martin", "Like success, failure is many things to many people. With a positive mental attitude, failure is a learning experience, a rung on the ladder, a plateau at which to get your thoughts in order and prepare to try again. – Clement Stone", "I’ve been absolutely terrified every moment of my life and I’ve never let it keep me from doing a single thing I wanted to do. – Georgia O’Keeffe", "Don’t give up. Don’t lose hope. Don’t sell out. – Christopher Reeve",  "The truest greatness lies in being kind, the truest wisdom in a happy mind. – Ella Wheeler Wilcox" ]

def show_frame():
	_, frame = stream.read()
	frame = cv2.flip(frame, 1)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = Image.fromarray(frame)
	frame = ImageTk.PhotoImage(image=frame)
	lmain.imagetk = frame
	lmain.configure(image=frame)
	lmain.after(10, show_frame)


def take_image():
	_, frame = stream.read()
	frame = cv2.flip(frame, 1)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	detector = FER(mtcnn=True)
	guess = detector.detect_emotions(frame)[0]["emotions"]["happy"] * 100

	g = ""
	if guess >= 75:
		g = random.choice(hq)
	elif guess >= 50:
		g = random.choice(mhq)
	elif guess >= 25:
		g = random.choice(msq)
	else:
		g = random.choice(sq)

	lbot.configure(text=f"{g}")


lmain = Label()
lmain.pack()

lbot = Label()
lbot.pack()

snapshot = Button(text="Play", command=take_image)
snapshot.pack()

show_frame()
window.lift()
window.mainloop()
