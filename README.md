
# 📝 AI Meeting Minutes Generator
An AI-powered tool that converts long meeting transcripts into **clear, concise, and actionable meeting minutes**.  
Built using **Hugging Face Transformers**, **PyTorch**, and **Streamlit**.

---

## 🚀 Features

### ✔️ Executive Summary Generation
Automatically summarizes long meeting transcripts using a transformer-based model (BART).

### ✔️ Action Items Extraction
Generates structured bullet-point action items from meeting discussions.

### ✔️ Long Transcript Support
Includes custom **text chunking** logic to process large transcripts exceeding model token limits.

### ✔️ Dual Input Options
- Paste transcript directly  
- Upload `.txt` file

### ✔️ Interactive Streamlit UI
Simple, clean, and user-friendly interface for real-time summarization.

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Model | BART (Hugging Face Transformers) |
| Framework | PyTorch |
| Frontend UI | Streamlit |
| Language | Python |
| Additional | SentencePiece, Custom Chunking |

---

## 📂 Project Structure

```
meeting-minutes-ai/
├── requirements.txt
├── src/
│   ├── summarizer.py       # Core summarization + action item extraction
│   └── chunking.py         # Splits long transcripts safely
├── app/
│   └── streamlit_app.py    # Streamlit UI
└── README.md
```

---

## 🔧 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/ai-meeting-minutes-generator.git
cd ai-meeting-minutes-generator
```

Create and activate a virtual environment:

```bash
python -m venv env
env\Scripts\activate  # Windows
# source env/bin/activate  # Mac/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

Start the Streamlit interface:

```bash
streamlit run app/streamlit_app.py
```

This will launch the app in your browser (usually at http://localhost:8501).

---

## 🧩 How It Works

### 1️⃣ Text Chunking
Large transcripts are split into overlapping chunks to avoid exceeding model token limits.

### 2️⃣ Chunk Summarization
Each chunk is summarized independently using BART.

### 3️⃣ Final High-Level Summary
Chunk summaries are combined and summarized again for coherence.

### 4️⃣ Action Items Extraction
A prompt-based summarization extracts actionable tasks discussed in the meeting.

---

## 📌 Sample Output

### Executive Summary
- High-level overview of discussion topics  
- Key decisions  
- Important updates and project priorities  

### Action Items
- Clear bullet points  
- Assigned responsibilities  
- Deadlines (if mentioned)

---

## 📁 Sample Input File  
You can test the tool using this sample transcript file:

🔗 **meeting_sample.txt**

---

## 🙌 Future Improvements

- Add audio-to-text using OpenAI Whisper  
- PDF export of meeting minutes  
- Multi-language support  
- Add "Decisions", "Risks", and "Next Steps" sections  
- Deploy as a web app (Streamlit Cloud / Render)

---

## 🤝 Contributing

Pull requests are welcome!  
If you'd like to suggest improvements, feel free to open an issue.

---

## ⭐ Show Your Support

If you find this project helpful, please ⭐ the repository to support it!

---

## 📬 Contact

**Vaibhav Pandey**  
LinkedIn: [my-profile  ](https://www.linkedin.com/in/vaibhav-pandey-02579a250/)
Email: your- vaibhavpanday245@gmail.com
