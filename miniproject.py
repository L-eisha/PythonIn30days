questions =[
{
    "prompt":"Who is known as the Missile Man of India",
    "options" : ["A: Vikram Sarabhai ", "B: A. P. J. Abdul Kalam" ,"C: Homi J. Bhabha" ,"D: Satish Dhawan"],
    "answer": "B ",
},
{
    "prompt":"Which is the largest planet in our Solar System?",
    "options":["A: Earth","B: Jupiter","C:Saturn" ,"D: Neptune"],
    "answer": "B ",
},
{
    "prompt": "The currency of Japan is:",
    "options": ["A: Yen", "B: Won", "C: Yuan", "D: Ringgit"],
    "answer": "A",

},
{   "prompt":"who invented telephone?",
    "options": ["A: Alexander Graham Bell", "B: Thomas Edison", "C: Nikola Tesla", "D: Guglielmo Marconi"],
    "answer": "A",
},
{
    "prompt":"capital of india ?",
    "options":["A:Amritsar","B:Ambala","C:new delhi ", "D:Bhopal",],
    "answer":"C"
},
{
    "prompt": "Which gas is most abundant in the Earth’s atmosphere?",
    "options": ["A: Oxygen", "B: Nitrogen", "C: Carbon Dioxide", "D: Hydrogen"],
    "answer": "B"
},

]



def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        if answer == question["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {question['answer']}\n")

    print(f"You got {score} out of {len(questions)} correct.")

run_quiz(questions)

