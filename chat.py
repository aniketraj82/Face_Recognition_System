# def chatbot_response(message):
#     # Normalize the message to lowercase for easier matching
#     msg = message.strip().lower()

#     # Greetings
#     if msg == "hii" or msg == "hi" or msg == "hello":
#         return "Namaskar! Welcome to Subharti University admission assistance. How can I help you today?"

#     # Admission questions
#     if "admission" in msg:
#         return (
#             "To apply for admission at Subharti University, please fill out the admission form available on our website or visit our admission office."
#         )

#     if "courses" in msg or "programs" in msg or "courses offered" in msg:
#         return (
#             "We offer a wide range of courses including engineering, medical, law, management, arts, and sciences. Please specify your area of interest for detailed information."
#         )

#     if "fee" in msg or "fees" in msg or "tuition" in msg:
#         return (
#             "Our fee structure varies by course. For undergraduate courses, fees start from 50,000 INR per year, and for postgraduate courses, fees start from 75,000 INR per year."
#         )

#     if "scholarship" in msg or "financial aid" in msg:
#         return (
#             "Subharti University offers scholarships based on merit and need. You can apply for scholarships after admission by submitting required documents at the scholarship office."
#         )

#     if "hostel" in msg or "accommodation" in msg:
#         return (
#             "Yes, we provide hostel facilities for both boys and girls with modern amenities and 24/7 security."
#         )

#     if "placements" in msg or "career" in msg or "job" in msg:
#         return (
#             "Our placement cell works with reputed companies to ensure good job opportunities for our students. We provide training and placement assistance throughout the year."
#         )

#     if "contact" in msg or "phone" in msg or "email" in msg:
#         return (
#             "You can contact us at: Phone: +91-1234567890, Email: admission@subharti.org"
#         )

#     if "thank" in msg or "thanks" in msg:
#         return "You're welcome! If you have any more questions, feel free to ask."

#     # Default fallback
#     return "Sorry, I didn't understand your question. Could you please rephrase or ask something else related to Subharti University admission?"


# # Simple interaction loop for testing
# if __name__ == "__main__":
#     print("Subharti University Chatbot (type 'exit' to quit)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             print("Chatbot: Thank you for chatting with us. Goodbye!")
#             break
#         response = chatbot_response(user_input)
#         print("Chatbot:", response)
import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline

# Load the question-answering model
try:
    qa_pipeline = pipeline("question-answering",
                           model="distilbert-base-cased-distilled-squad")
except Exception as e:
    messagebox.showerror("Model Error", f"Error loading model:\n{e}")
    exit()

# Knowledge base for model-based Q&A
knowledge_base = """
ChatGPT is an AI chatbot developed by OpenAI. It uses the GPT language model to understand and respond to user input. 
It can perform tasks like answering questions, writing text, solving problems, and simulating conversation.
"""


class Help:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Offline Chatbot")
        self.root.geometry("700x600")

        self.chat_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Arial", 12), state='normal')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.insert(
            tk.END, "🤖 subhartian: Welcome to Subharti University.\nHello! Ask me something about admission-related questions.\n\n")

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", lambda event: self.send_message())

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=(0, 10))

        send_btn = tk.Button(btn_frame, text="Send",
                             command=self.send_message, width=12)
        send_btn.grid(row=0, column=0, padx=5)

        help_btn = tk.Button(btn_frame, text="Help",
                             command=self.open_help, width=12)
        help_btn.grid(row=0, column=1, padx=5)

        self.root.mainloop()

    def chatbot_response(self, msg):
        msg = msg.strip().lower()

        if msg in ["hii", "hi", "hello"]:
            return "Namaskar! Welcome to Subharti University admission assistance. How can I help you today?"

        if "admission" in msg or "apply" in msg:
            return "To apply for admission at Subharti University, please fill out the admission form available on our website or visit our admission office."

        if "courses" in msg or "programs" in msg or "courses offered" in msg:
            return "We offer a wide range of courses including engineering, medical, law, management, arts, and sciences. Please specify your area of interest for detailed information."

        if "fee" in msg or "fees" in msg or "tuition" in msg:
            return "Our fee structure varies by course. For undergraduate courses, fees start from 50,000 INR per year, and for postgraduate courses, fees start from 75,000 INR per year."

        if "scholarship" in msg or "financial aid" in msg:
            return "Subharti University offers scholarships based on merit and need. You can apply for scholarships after admission by submitting required documents at the scholarship office."

        if "hostel" in msg or "accommodation" in msg:
            return "Yes, we provide hostel facilities for both boys and girls with modern amenities and 24/7 security."

        if "placements" in msg or "career" in msg or "job" in msg:
            return "Our placement cell works with reputed companies to ensure good job opportunities for our students. We provide training and placement assistance throughout the year."

        if "library" in msg or "book" in msg or "books" in msg:
            return "The university library is well-stocked with academic books, journals, and digital resources accessible to all students."

        if "contact" in msg or "phone" in msg or "email" in msg:
            return "You can contact us at: Phone: +91-1234567890, Email: admission@subharti.org"

        if "B.Tech fee" in msg or "b.tech and fee" in msg:
            return "The fee for B.Tech at Subharti University is INR 2.07 Lakh. Q: What is the fee for M.Tech at Subharti University? A: The fee for M.Tech at Subharti University is INR 1.31 Lakh."

        if "location" in msg or "where" in msg:
            return "Subharti University is located in Meerut,NH-58 Delhi Haridwar Road, Uttar Pradesh, India."

        if "ugc" in msg or "approved" in msg or "recognised" in msg:
            return "Yes, Subharti University is recognized by the UGC and accredited by relevant authorities."

        if "sports" in msg or "gym" in msg:
            return "Yes, we have excellent sports facilities and a modern gym for students."

        if "Campus" in msg or "campus" in msg or "hostel" in msg or "kitna hostel h" in msg or "area" in msg:
            return "The university is situated on a 250-acre campus in Meerut, in the National Capital Region of India. It includes a 1042-bed hospital and an auditorium with 2,500 seating capacity. There are 13 hostels for students and ten residential complexes for faculty members and staff."

        if "rani gaidinliu" in msg or "girls hostel" in msg or "rani" in msg:
            return "Rani Gaidinliu Girls Hostel is one of the dedicated residential facilities for female students at Swami Vivekanand Subharti University, Meerut. The hostel provides a safe, secure, and comfortable living environment with amenities such as 24/7 security, mess facilities, Wi-Fi, and recreational areas."

        if "Is Subharti University Good for Distance MBA" in msg or "distance" in msg:
            return ("Subharti University, established in 2008 and located in Meerut, Uttar Pradesh, is a private institution offering both regular and distance learning programs. Since 2009, it has been providing UGC-DEB approved distance education across various disciplines.\n"
                    "The university is especially recognized for its Distance MBA program, considered one of the best in India. It is a two-year postgraduate degree designed for students and working professionals who cannot attend regular classes. "
                    "The program equips learners with essential business and management skills in areas like communication, human resources, and product management. Subharti’s distance MBA uses modern technology and online resources to deliver quality education. "
                    "Students benefit from flexible learning, exposure to expert faculty, peer interaction, and industry-relevant training. The curriculum mirrors traditional MBA programs, ensuring no compromise on quality. Ideal for women and working professionals, "
                    "the program offers strong career prospects across public and private sectors, and promotes critical thinking, networking, and specialization in emerging business fields.")

        if "thank" in msg or "thanks" in msg:
            return "You're welcome! If you have any more questions, feel free to ask."

        return None

    def send_message(self):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.chat_area.insert(tk.END, f"You: {user_input}\n")
        self.entry.delete(0, tk.END)

        response = self.chatbot_response(user_input)
        if response:
            self.chat_area.insert(tk.END, f"🤖 subhartian: {response}\n\n")
        else:
            try:
                answer = qa_pipeline(question=user_input,
                                     context=knowledge_base)['answer']
                self.chat_area.insert(tk.END, f"🤖 subhartian: {answer}\n\n")
            except Exception:
                self.chat_area.insert(
                    tk.END, "🤖 subhartian: Sorry, I couldn't understand your question.\n\n")

        self.chat_area.see(tk.END)

    def open_help(self):
        help_win = tk.Toplevel(self.root)
        help_win.title("Help")
        help_win.geometry("400x250")
        help_text = (
            "💬 How to use:\n"
            "- Type your question in the text box.\n"
            "- Press Enter or click Send.\n\n"
            "🤖 Example Questions:\n"
            "- What is the admission process?\n"
            "- Do you have hostel facilities?\n"
            "- What courses are offered?\n"
            "- What is ChatGPT?\n\n"
            "Note: The chatbot works offline with a local knowledge base and predefined answers."
        )
        label = tk.Label(help_win, text=help_text,
                         font=("Arial", 11), justify="left")
        label.pack(padx=20, pady=20)


# Run the chatbot
if __name__ == "__main__":
    Help()
