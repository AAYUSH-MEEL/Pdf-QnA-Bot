<img width="1916" height="962" alt="Screenshot 2025-10-04 001545" src="https://github.com/user-attachments/assets/f66322ec-5bf0-44bd-af75-f8fde4c9bc16" />

# PDF QnA Bot

An AI-powered chatbot that allows users to upload PDF documents and ask questions to get answers based on the content of the uploaded PDF. Built using Streamlit, Langchain, and Groq API.

## Features

- Upload PDF documents
- Ask questions related to the PDF content
- Get AI-generated answers using retrieval-augmented generation (RAG)
- User-friendly interface with Streamlit

## Requirements

- Python 3.8 or higher
- Streamlit
- PyPDF2
- Langchain (text_splitters, huggingface, community, groq)
- FAISS (for vector storage)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AAYUSH-MEEL/Pdf-QnA-Bot.git
   cd Pdf-QnA-Bot
   ```

2. Install the required packages:
   ```
   pip install streamlit PyPDF2 langchain langchain-huggingface langchain-community langchain-groq faiss-cpu
   ```

3. Set up your Groq API key:
   - Obtain an API key from [Groq](https://groq.com/)
   - Set the environment variable:
     ```
     export GROQ_API_KEY="your_api_key_here"
     ```
     Or add it to your `.env` file and load it in the code.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run venv/chatbot.py
   ```

2. Open the app in your browser (usually at http://localhost:8501)

3. Upload a PDF document using the sidebar.

4. Enter your question in the text input field.

5. View the AI-generated answer based on the PDF content.

## Project Structure

- `venv/chatbot.py`: Main application file
- `README.md`: This file
- `TODO.md`: Project tasks and notes

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is open-source. Please check the license file for details.


