# RAVEN - The Gemini Chatbot 🐦‍⬛

RAVEN is an AI-powered chatbot built with **Streamlit** and powered by the **Gemini 1.5 Flash model** for natural language processing. It provides seamless, real-time conversations through an intuitive and interactive interface.

---

## 🚀 Features

✅ **Interactive Chat** – Real-time responses with context awareness.  
✅ **User-Friendly Interface** – Built with Streamlit for a smooth experience.  
✅ **Session History** – Keeps track of past messages for continuity.  
✅ **Configurable Settings** – Customize model parameters (temperature, top-p, top-k, token limits).  

---

## 🖼️ Screenshots

![Screenshot](https://github.com/IAnuragMahapatra/gemini-1.5-flash-streamlit-chatbot/blob/386d4e4f3ac70920a1354e413d1a23ce1490d255/Screenshots/Screenshot1.png)

---

## 🌐 Hosted Link

Try RAVEN live:  
🔗 **[RAVEN - The Gemini Chatbot](https://gemini-15-flash-app-chatbot.streamlit.app/)**

---

## ⚙️ Configuration Settings

| Parameter           | Value  |
|---------------------|--------|
| **Temperature**     | 1      |
| **Top-p**          | 0.95   |
| **Top-k**          | 64     |
| **Max Output Tokens** | 8192  |
| **Response MIME Type** | `text/plain` |

---

## 🛠️ Local Setup

Follow these steps to set up and run RAVEN on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/IAnuragMahapatra/gemini-1.5-flash-streamlit-chatbot.git
cd gemini-1.5-flash-streamlit-chatbot
```

### 2️⃣ Install Dependencies
```bash
pip install streamlit google-generativeai python-dotenv
```

### 3️⃣ Configure API Key  
Choose one of the two methods to set up your **Google API key**.

#### 🔹 Method 1: Using `.env` File
1. Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```
2. Add your **Google API key**:
   ```text
   GOOGLE_API_KEY=<your-api-key>
   ```
3. Load the key in your code:
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
   ```

#### 🔹 Method 2: Using Streamlit Secrets  
1. Create a `secrets.toml` file:
   ```bash
   mkdir -p ~/.streamlit
   echo "[secrets]" > ~/.streamlit/secrets.toml
   echo "GOOGLE_API_KEY='<your-api-key>'" >> ~/.streamlit/secrets.toml
   ```
2. Access the key in your code:
   ```python
   GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
   ```

### 4️⃣ Run the Application
```bash
streamlit run main.py
```

### 5️⃣ Access the App  
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🏗️ Technologies Used

- **Python** – Core logic and API integration.  
- **Streamlit** – Web framework for UI.  
- **Google Generative AI** – Gemini 1.5 Flash model for NLP.  
- **dotenv** – Environment variable management.  

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to modify and distribute it.

---

## 📧 Contact

📌 **Author**: Anurag Mahapatra  
📩 **Email**: [anurag2005om@gmail.com](mailto:anurag2005om@gmail.com)  

Enjoy chatting with **RAVEN** 🐦‍⬛!
