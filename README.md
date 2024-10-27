# RAVEN - The Gemini Chatbot 🐦‍⬛

RAVEN is a chatbot application built using **Streamlit** and powered by the **Gemini 1.5 Flash model** for natural language processing. It enables seamless conversations with users through a simple and interactive interface.

## Features
- **Interactive Chat**: Real-time responses powered by the Gemini 1.5 Flash model.
- **User-Friendly Interface**: Built with Streamlit for a responsive web experience.
- **Session History**: Maintains chat history for context-aware interactions.
- **Customizable Configuration**: Adjust model parameters like temperature, top-p, top-k, and token limits.

## Hosted Link
Try the chatbot live here:  
🔗 **[RAVEN - The Gemini Chatbot](https://gemini-15-flash-app-chatbot.streamlit.app/)**

---

## Configuration Settings
- **Temperature**: 1  
- **Top-p**: 0.95  
- **Top-k**: 64  
- **Max Output Tokens**: 8192  
- **Response MIME Type**: `text/plain`

---

## Local Setup

Follow these steps to set up the chatbot on your local machine.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Dependencies
```bash
pip install streamlit google-generativeai python-dotenv
```

### 3. Configure API Key  
You can use **either** of the two methods below to configure your Google API key:

---

### Method 1: Using `.env` File
1. Create a `.env` file in the root of the project:
   ```bash
   touch .env
   ```
2. Add your **Google API key** in the `.env` file:
   ```text
   GOOGLE_API_KEY=<your-api-key>
   ```
3. Update the code to load the key from `.env`:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()  # Load environment variables from .env
   GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
   ```

---

### Method 2: Using Streamlit Secrets  
1. Create a `secrets.toml` file:
   ```bash
   mkdir -p ~/.streamlit
   echo "[secrets]" > ~/.streamlit/secrets.toml
   echo "GOOGLE_API_KEY='<your-api-key>'" >> ~/.streamlit/secrets.toml
   ```
2. Update your code to access the API key from Streamlit secrets:
   ```python
   GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
   ```

---

### 4. Run the Application
```bash
streamlit run app.py
```

### 5. Access the App
Open [http://localhost:8501](http://localhost:8501) in your browser to access the chatbot.

---

## Technologies Used
- **Python**: Backend logic and model integration  
- **Streamlit**: Frontend framework for building the web application  
- **Google Generative AI**: Powered by the Gemini 1.5 Flash model for NLP  
- **dotenv**: For environment variable management  

---

## License
This project is licensed under the **MIT License**. Feel free to modify and distribute it.

---

Enjoy chatting with **RAVEN** 🐦‍⬛!
