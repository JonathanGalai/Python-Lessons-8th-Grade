from google import genai

client = genai.Client()

questions_subject = input("What is the subject for the 5 trivia questions?\n")

prompt = ("Write 5 trivia questions about " + questions_subject + ".\n"
          "Question 1 is very easy, and each question is harder than the one before. "
          "Question 5 is very hard.\n"
          "Write only the questions, one per line, with no numbers and no answers.")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

text = response.text

# Split the answer into lines and skip empty ones
lines = []
for line in text.split("\n"):
    if line.strip() != "":
        lines.append(line.strip())

# Put each question into its own string variable
question1 = lines[0]
question2 = lines[1]
question3 = lines[2]
question4 = lines[3]
question5 = lines[4]

print("Easy:", question1)
print("Medium-easy:", question2)
print("Medium:", question3)
print("Hard:", question4)
print("Very hard:", question5)
