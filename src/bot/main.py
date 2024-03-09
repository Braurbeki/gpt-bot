import gptapi


geography_questions = [
    "What is the capital of Ukraine?",
    "What is the population of Zimbabwe?",
    "Which continent has the most countries?",
]



if __name__ == '__main__':
    for q in geography_questions:
        print(q)
        print("Your answer: ", end =" ")
        user_aswr = input()

        is_correct, bot_answer = gptapi.process_question(q, user_aswr)

        print(f'\nAnswer is correct: {is_correct}')
        print(f'Bot answered: {bot_answer}\n')