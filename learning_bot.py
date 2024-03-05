import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base['questions']:
        if q['question'] == question:
            return q['answer']
    return None

def remove_question_from_knowledge_base(question: str, knowledge_base: dict):
    for i, q in enumerate(knowledge_base['questions']):
        if q['question'] == question:
            del knowledge_base['questions'][i]
            save_knowledge_base('knowledge_base.json', knowledge_base)
            print("Bot: The question-answer pair has been successfully removed.")
            return
    print("Bot: Question not found in the knowledge base.")

def chatbot():
    knowledge_base = load_knowledge_base('knowledge_base.json')
    
    while True:
        user_question = input('You: ')
        
        if user_question.lower() == 'quit':
            break
        elif user_question.lower() == 'remove question':
            question_to_remove = input('Which question would you like to remove? ')
            remove_question_from_knowledge_base(question_to_remove, knowledge_base)
            continue
        
        best_match = find_best_match(user_question, [q['question'] for q in knowledge_base['questions']])
        
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I am sorry, I do not know the answer to your question. Can you teach me?')
            new_answer = input('Type the answer or \'skip\' to skip: ')
            
            if new_answer.lower() != 'skip':
                knowledge_base['questions'].append({'question': user_question, 'answer': new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you for teaching me!')

if __name__ == '__main__':
    chatbot()
