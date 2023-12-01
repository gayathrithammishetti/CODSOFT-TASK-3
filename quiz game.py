import tkinter as tk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.background_image = tk.PhotoImage(file="Quiz-Logo-PNG-Image.png")


        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)



        self.questions = [
            "1. What country has the highest life expectancy?",
            "2. What company was originally called 'cadabra'?",
            "3. Which planet in the Milky Way is the hottest?",
            "4. What city is known as 'The Eternal City'?",
            "5. Which planet has the most moons?"
        ]

        self.options = [
            ["India", "Hong Kong", "Australia", "Algeria"],
            ["Amazon", "Flipkart", "Google", "Microsoft"],
            ["Earth", "Venus", "Saturn", "Jupiter"],
            ["Rome", "Berlin", "Paris", "Seoul"],
            ["Jupiter", "Saturn", "Venus", "Uranus"]
        ]

        self.answers = [
            "Hong Kong",
            "Amazon",
            "Venus",
            "Rome",
            "Saturn"
        ]

        self.score = 0
        self.current_question = 0

    
        self.user_ans = tk.StringVar()
        self.user_ans.set('None')

        self.user_score = tk.IntVar()
        self.user_score.set(0)

        tk.Label(root, text="Quiz App", font="Arial 40 bold", relief=tk.SUNKEN, background="cyan", padx=10, pady=9).pack()
        tk.Label(root, text="", font="Arial 10 bold").pack()

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, font="Arial  17 bold")
        self.start_button.pack()

        self.f1 = tk.Frame(root)
        self.f1.pack(side=tk.TOP, fill=tk.X)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font="Arial 17 bold")

    def start_quiz(self):
        self.start_button.forget()
        self.next_button.pack()
        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            self.check_ans()
            self.user_ans.set('None')
            c_question = self.questions[self.current_question]
            self.clear_frame()
            tk.Label(self.f1, text=f"Question: {c_question}", padx=15, font="Arial 18 normal").pack(anchor=tk.NW)
            for option in self.options[self.current_question]:
                tk.Radiobutton(self.f1, text=option, variable=self.user_ans, value=option, padx=28).pack(anchor=tk.NW)
            self.current_question += 1
        else:
            self.next_button.forget()
            self.check_ans()
            self.clear_frame()
            output = f"Your score is {self.user_score.get()} out of {len(self.questions)}"
            tk.Label(self.f1, text=output, font="Arial 25 bold").pack()
            tk.Label(self.f1, text="Thanks for participating", font="Arial 20 bold").pack()

    def check_ans(self):
        temp_ans = self.user_ans.get()
        if temp_ans != 'None' and temp_ans == self.answers[self.current_question - 1]:
            self.user_score.set(self.user_score.get() + 1)

    def clear_frame(self):
        for widget in self.f1.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("850x520")
    root.minsize(800, 400)

    quiz_game = QuizGame(root)

    root.mainloop()
