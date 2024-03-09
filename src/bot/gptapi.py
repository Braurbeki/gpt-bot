import openai

# Set your API key here
#client = openai.OpenAI(api_key="")

# Sends request through OpenAI API. 
# Returns bool identifing whether the answer was true, and response from the bot
def process_question(question: str, userAnswer: str) -> (bool, str):
    
    msgs_to_send = [
            {"role": "system", "content": "You are geography bot. " +
             "You should provide a short answer starting with \"Yes./No.\" whether the answer to provided question is correct. If not - the correct answer and small explanation if nessesary. If answer is partially correct - accept it!"},
            {"role": "user", "content": f"Question: {question}. Answer: {userAnswer}"}
        ]


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs_to_send
    )

    msg_content = completion.choices[0].message.content

    return msg_content.count("Yes.") > 0, msg_content
    
    