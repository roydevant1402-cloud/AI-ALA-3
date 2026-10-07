# Rule-Based College Information Chatbot
# Name: Roy Devant
# Enrollment Number: 241105060114
# Branch: Diploma (I.T)
# Semester: 5th Semester
# Subject: AI Artificial Intelligence

print("==============================================")
print("       COLLEGE INFORMATION CHATBOT")
print("==============================================")
print("Hello! I am a simple rule-based college chatbot.")
print("You can ask about courses, admission, library, fees,")
print("timings, exams, or contact information.")
print("Type 'bye' to exit.")
print()

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Thank you for chatting. Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! How can I help you with college information?")

    elif "course" in user_input or "courses" in user_input:
        print("Bot: The college offers Diploma and other technical courses. "
              "Please contact the college office for the current course list.")

    elif "admission" in user_input or "admissions" in user_input:
        print("Bot: Admission information is available from the college admission office. "
              "Please check the official notice or contact the office.")

    elif "library" in user_input:
        print("Bot: The college library provides textbooks, reference books, "
              "and study materials for students.")

    elif "fee" in user_input or "fees" in user_input:
        print("Bot: Fee details depend on the course and semester. "
              "Please contact the accounts office for the latest fee structure.")

    elif "timing" in user_input or "time" in user_input or "hours" in user_input:
        print("Bot: College working hours are generally during regular daytime hours. "
              "Please confirm the current timetable with the college office.")

    elif "exam" in user_input or "examination" in user_input:
        print("Bot: Examination dates and schedules are announced through official college notices.")

    elif "contact" in user_input or "phone" in user_input:
        print("Bot: For official contact details, please refer to the college website "
              "or contact the college office.")

    elif "thank" in user_input:
        print("Bot: You're welcome! I am happy to help.")

    else:
        print("Bot: Sorry, I do not understand that question. "
              "Please ask about courses, admission, library, fees, timings, exams, or contact information.")

print("Chatbot program ended.")
