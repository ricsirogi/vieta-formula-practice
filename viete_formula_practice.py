import random
import time
import tkinter as tk


class App():
    def __init__(self):
        random.seed(time.time())
        self.GENERAL_FONT = ("Consolas", 20)
        self.num_range = (-10, 10)
        self.x1, self.x2 = 0, 0
        self.showing_ans = True

        self.best_time = 9999
        self.last_time = 0
        self.start_time = time.time()

        self.root = tk.Tk()
        self.root.title("Viete formula practice")
        self.equation_label = tk.Label(self.root, font=self.GENERAL_FONT, width=20)
        self.last_time_label = tk.Label(self.root, font=self.GENERAL_FONT, text="Last:00.00")
        self.best_time_label = tk.Label(self.root, font=self.GENERAL_FONT, text="Best:00.00")
        self.ans_label = tk.Label(self.root, font=self.GENERAL_FONT)
        self.continue_button = tk.Button(self.root, font=self.GENERAL_FONT,
                                         text="Continue", height=5, command=self.click)

        self.equation_label.grid(row=0, column=0, columnspan=2, sticky="n")
        self.last_time_label.grid(row=1, column=0, sticky="nw")
        self.best_time_label.grid(row=1, column=1, sticky="ne")
        self.ans_label.grid(row=2, column=0, columnspan=2, sticky="")
        self.continue_button.grid(row=0, column=2, rowspan=3, sticky="ns")

        self.click()

        self.root.mainloop()

    def generate_roots(self, num_range: tuple[int, int]) -> tuple[int, int, int, float, float]:
        """
        This function takes a range that the two roots should be in 
        and calculates a, b and c\n
        If the randomly generated roots result in either b or c being 0,
        the function recursively calls itself until it meets this requirement.\n
        If either b or c is 0 then the equation becomes a non-quadratic equation.
        """
        x1, x2 = num_range[0]-1, num_range[0]-1
        while True:
            x1 = random.randint(num_range[0], num_range[1])
            x2 = random.randint(num_range[0], num_range[1])
            # This adds more randomness, so we don't get the same value for a and b twice
            # Basically, at least one number is going to be different every time
            # There's an 'or' instead of an 'and' because this way the user can't think:
            # "Last time x1 was 4, so this time it CAN'T be 4 again!"
            # You're wrong Billy, it can be 4 again...
            if (x1 != self.x1 and x1 != self.x2) or (x2 != self.x1 and x2 != self.x2):
                break

        self.x1 = str(x1)
        self.x2 = str(x2)

        a = 1
        b = -((x1 + x2) / a)
        c = (x1 * x2) / a

        return (x1, x2, a, b, c) if b != 0 and c != 0 else self.generate_roots(num_range)

    def generate_time_string(self, time: float) -> str:
        """
        Takes in a float number which represents a time (to beat the problem) in seconds\n
        Returns the time in 02.12 format where 02 is the second and .12 is the decimal
        """
        s_time = str(round(time, 2))
        if time < 10:
            s_time = "0" + s_time

        return s_time[0:s_time.find(".")] + "." + s_time[s_time.find(".") + 1:]

    def click(self):
        if self.showing_ans:
            _, _, a, b, c = self.generate_roots(self.num_range)

            if a == 1:
                b, c = int(b), int(c)

            equation = f"{a if a != 1 else ''}x^2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c} = 0"
            self.equation_label["text"] = equation
            self.ans_label["text"] = "x1:\nx2:"

            self.showing_ans = False
            self.start_time = time.time()
        else:
            self.ans_label["text"] = f"x1:{self.x1}\nx2:{self.x2}"
            self.showing_ans = True

            time_to_beat = time.time() - self.start_time
            self.last_time = time_to_beat
            self.last_time_label["text"] = "Last:" + self.generate_time_string(self.last_time)
            if time_to_beat < self.best_time:
                self.best_time = round(time_to_beat, 2)
                self.best_time_label["text"] = "Best:" + self.generate_time_string(self.last_time)


if __name__ == "__main__":
    app = App()
