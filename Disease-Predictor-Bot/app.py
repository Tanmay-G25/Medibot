from tkinter import *
from chat import get_response, bot_name

BG_COLOR = "#C1EEFF"
# "#17202A" 
BG_GRAY = "#655356"
# "#ABB2B9"
TEXT_COLOR="#C1EEFF"
# "#EAECEE" 
USER_CONSOLE_COLOR = "#28231C"


FONT="Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

	def __init__(self):
		self.window= Tk()
		self._setup_main_window()

	def run(self):
		self.window.mainloop()

	def _setup_main_window(self):
		self.window.title("Disease identifier")
		self.window.resizable(width=True, height=True) 
		self.window.configure(width=700, height=500, bg=BG_COLOR)

		# heading
		head_label = Label(self.window, bg=USER_CONSOLE_COLOR, fg=TEXT_COLOR, text="Disease Predictor", font=FONT_BOLD, pady=7)
		head_label.place(relwidth=1)

		# separator
		line = Label(self.window, width=450, bg=BG_GRAY) 
		line.place(relwidth=1, rely=0.07, relheight=0.012)

		# text settings
		self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg= USER_CONSOLE_COLOR, font=FONT, padx=7, pady=7)
		self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08) 
		self.text_widget.configure(cursor="arrow", state=DISABLED)


		#initial text
		init_text = 'Please describe your symptoms:\n\n'
		self.text_widget.configure(state=NORMAL) 
		self.text_widget. insert (END, init_text) 
		self.text_widget.configure(state=DISABLED)

		# bottom label
		bottom_label = Label(self.window, bg=BG_GRAY, height=80) 
		bottom_label.place(relwidth=1, rely=0.825)
 	

		self.init_text = Entry(bottom_label, bg=USER_CONSOLE_COLOR, fg=TEXT_COLOR, font=FONT) 
		self.init_text.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011) 
		self.init_text.focus()

		# message entry box
		self.symptom_entry = Entry(bottom_label, bg=USER_CONSOLE_COLOR, fg=TEXT_COLOR, font=FONT, insertbackground = 'white') 
		self.symptom_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011) 
		self.symptom_entry.focus()
		self.symptom_entry.bind("<Return>", self._on_enter_pressed)

		# predict button
		predict_button = Button(bottom_label, text="Predict", fg = BG_COLOR, font=FONT_BOLD, width=20, bg=BG_GRAY, 
				command=lambda: self._on_enter_pressed(None))
		predict_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

	def _on_enter_pressed(self, event):
		symptom = self.symptom_entry.get()
		self._insert_message(symptom, "You: ") 


	def _insert_message(self, symptom, sender):
		if not symptom: 
			return

		self.symptom_entry.delete(0, END)
		userInput = f'{sender}:{symptom}\n'
		self.text_widget.configure(state=NORMAL) 
		self.text_widget. insert (END, userInput) 
		self.text_widget.configure(state=DISABLED)


		reply= f"\n{bot_name}: \n{get_response(symptom)}\n\n"
		self.text_widget.configure(state=NORMAL) 
		self.text_widget. insert (END, reply) 
		self.text_widget.configure(state=DISABLED)
		self.text_widget.see(END)
		
if __name__ == "__main__":
	app = ChatApplication()
	app.run()