# LEARNING-BOT
### How It Works

This interactive chatbot is designed to continuously learn and improve its ability to respond to user queries by updating its knowledge base with new question-answer pairs. Here's a quick guide on how it operates:

1. **Starting the Chatbot**: To begin interacting with the chatbot, run the Python file (`learning_bot.py`). This initializes the chatbot and loads its knowledge base from a JSON file.

3. **Interacting with the Chatbot**: Once the chatbot is running, you can ask it any question by simply typing it into the console. The chatbot will attempt to find the best match for your question within its knowledge base and provide you with an answer.

4. **Teaching the Chatbot**: If the chatbot doesn't know the answer to your question, it will prompt you to teach it. You can input the correct answer, and the chatbot will save this new question-answer pair to its knowledge base, thereby learning from the interaction.

5. **Removing a Question**: If you wish to remove a question from the chatbot's knowledge base, type 'remove question' when prompted for your query. The chatbot will then ask you to specify the exact question you want to remove. Once identified, the question-answer pair will be permanently deleted from the knowledge base, keeping the chatbot's information accurate and relevant.

6. **Automatic Saving**: All changes to the knowledge base, including newly added question-answer pairs and removals, are automatically saved to the JSON file. This ensures that the chatbot's knowledge is persistent across sessions, allowing it to learn and grow over time.

By following these steps, users can interact with, teach, and maintain the chatbot, making it a versatile tool for educational purposes, customer support, or as a stepping stone towards developing more sophisticated AI-driven conversational systems.
