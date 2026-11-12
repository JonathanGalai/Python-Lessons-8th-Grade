from google import genai
from google.genai import types, errors
import turtle
import time

client = genai.Client(api_key=AQ.Ab8RN6Ixir9K9l3TiwejYojBMFDBXY4VTGm-mVVTE1ifDUhDHA)
MODEL = "gemini-3.5-flash"
BACKUP_MODEL = "gemini-2.5-flash"

sc = turtle.Screen()
sc.setup(800, 700)
sc.bgcolor("cyan")

player = turtle.Turtle()
player.hideturtle()
player.pu()


def ask_gemini(request: str) -> str:
    # if the model is busy (503), wait and try again, then try a backup model
    for model in [MODEL, BACKUP_MODEL]:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=request,
                    config=types.GenerateContentConfig(temperature=0.9),
                )
                return response.text.strip()
            except errors.ServerError:
                show_message(f"Gemini is busy...\ntrying again ({attempt + 1}/3)", size=20)
                time.sleep(3)
    return ""


def show_message(text, size=24):
    player.clear()
    player.goto(0, 0)
    player.write(text, align="center", font=("Arial", size, "bold"))


def show_clues(subjects, clues):
    player.clear()
    y = 280
    player.goto(0, y)
    player.write("Guess the words!", align="center", font=("Arial", 26, "bold"))
    y -= 50
    for i in range(len(subjects)):
        player.goto(-370, y)
        player.write(f"{i + 1}. {subjects[i]}:", align="left", font=("Arial", 16, "bold"))
        y -= 28
        player.goto(-350, y)
        player.write(clues[i], align="left", font=("Arial", 14, "normal"))
        y -= 45


def normalize(text):
    return text.strip().lower()


# --- 1. how many subjects (3 or 4) ---
num_subjects = turtle.numinput("Alias", "כמה נושאים? (3 או 4)", default=3, minval=3, maxval=4)
if num_subjects is None:
    turtle.bye()
    exit()
num_subjects = int(num_subjects)

show_message(f"Welcome to Alias!\nGive me {num_subjects} subjects")

# --- 2. get the subjects ---
subjects = []
for i in range(num_subjects):
    subject = turtle.textinput(f"נושא {i + 1} מתוך {num_subjects}", "הכנס נושא (למשל: ספורט, טבע):")
    if subject is None:
        turtle.bye()
        exit()
    subjects.append(subject.strip())

show_message("Gemini is thinking of words...")

# --- 3. ask Gemini for one word + one clue per subject ---
prompt_template = f"""
You are running a word guessing game for a 13 year old student.
For each of these {num_subjects} subjects, pick ONE English word related to it:
{", ".join(subjects)}

For each word write a short clue in English (one sentence, max 12 words)
that helps guess the word. Never write the word itself in the clue.

Answer with exactly {num_subjects} lines, in the same order as the subjects.
Each line must look like this:
word | clue
No numbers, no extra text.
"""

answer = ask_gemini(prompt_template)

words = []
clues = []
for line in answer.splitlines():
    if "|" in line:
        word, clue = line.split("|", 1)
        words.append(word.strip())
        clues.append(clue.strip())

if len(words) != num_subjects:
    show_message("Gemini got confused :(\nRun the game again", size=20)
    turtle.mainloop()
    exit()

# --- 4. show all clues, the player answers in order ---
show_clues(subjects, clues)

guess_text = turtle.textinput("התשובות שלך", f"כתוב {num_subjects} מילים לפי הסדר, מופרדות בפסיק:")
if guess_text is None:
    guess_text = ""
guesses = guess_text.split(",")

# --- 5. check the answers ---
score = 0
results = ""
for i in range(num_subjects):
    if i < len(guesses):
        guess = guesses[i]
    else:
        guess = ""

    if normalize(guess) == normalize(words[i]):
        score += 1
        results += f"{i + 1}. {words[i]} ✅\n"
    else:
        results += f"{i + 1}. {words[i]} ❌ (you wrote: {guess.strip()})\n"

show_message(f"{results}\nYOUR SCORE: {score}/{num_subjects}", size=20)
turtle.mainloop()
