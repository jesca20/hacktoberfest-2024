flashcards = {
    "Capital of France": "Paris",
    "Largest planet in the Solar System": "Jupiter",
    "Python keyword for functions": "def"
}

def quiz():
    score = 0
    for question, answer in flashcards.items():
        response = input(f"{question}? ")
        if response.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    print(f"Your final score: {score}/{len(flashcards)}")

quiz()
