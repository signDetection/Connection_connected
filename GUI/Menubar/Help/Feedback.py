from tkinter import *
from tkinter import messagebox


class Feedback:

    def __init__(self, feedback_window):
        feedback_window.title('Feedback To conversation connected')
        feedback_window.resizable(False, False)
        feedback_window.configure(background="AliceBlue")

        self.frame_header = Frame(feedback_window, background="AliceBlue")  # header frame
        self.frame_header.pack()

        Label(self.frame_header,
              text="Thank you for your valuable feedback !!! ",
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 18, 'bold')).grid(row=0, column=1)

        Label(self.frame_header,
              text="We're glad you chose to conversation connected !!!\nPlease tell us how it was!",
              fg="DarkSlateGray",
              bg="AliceBlue",
              justify='center').grid(row=1, column=1)

        self.frame_content = Frame(feedback_window, background="AliceBlue")  # content frame
        self.frame_content.pack()

        Label(self.frame_content,
              text='Name:',
              fg="DarkSlateGray",
              bg="AliceBlue").grid(row=0, column=0, padx=5, sticky='sw')
        Label(self.frame_content,
              text='Email:',
              fg="DarkSlateGray",
              bg="AliceBlue").grid(row=0, column=2, padx=5, sticky='sw')
        Label(self.frame_content,
              text='Comments:',
              fg="DarkSlateGray",
              bg="AliceBlue").grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = Entry(self.frame_content, width=24)
        self.entry_email = Entry(self.frame_content, width=24)
        self.text_comments = Text(self.frame_content, width=50, height=10, font=('Times New Roman', 10))

        self.entry_name.grid(row=1, column=0, columnspan=2, padx=5)
        self.entry_email.grid(row=1, column=2, columnspan=2, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        Button(self.frame_content,
               text='Give Feedback',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "italic"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=self.submit).grid(row=4, column=1, padx=5, pady=10,
                                         sticky='e')
        Button(self.frame_content,
               text='Clear',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "italic"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=self.clear).grid(row=4, column=2, padx=15, pady=10,
                                        sticky='w')
        Button(self.frame_content,
               text='Close',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "italic"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=feedback_window.destroy).grid(row=4, column=4, padx=5,
                                                     pady=10,
                                                     sticky='e')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title="Feedback to conversation connected", message="Comments Submitted!")
        global feedback_window
        feedback_window.destroy()

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def feedback():
    global feedback_window
    feedback_window = Tk()
    Feedback(feedback_window)
    feedback_window.mainloop()


if __name__ == "__main__":
    feedback()
