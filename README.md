
# LinkedIn Profile Analyzer (AI-Powered)

A Django-based web application that analyzes LinkedIn profile content (manually entered) using AI and NLP techniques to provide feedback on grammar, tone, and relevance for three major sections: **Headline**, **Skills**, and **About**.

---

## Key Features

-  Analyze LinkedIn **Headline**, **Skills**, and **About** sections
-  AI/NLP analysis using:
  - `language_tool_python` (Grammar & style)
  - `TextBlob` (Sentiment & grammar)
  - `VADER` (Tone & emotion)
  - `transformers` or `OpenAI API` (Contextual relevance)
-  Instant feedback with suggestions
-  User-friendly Django web interface
-  No login required (manual input only)

---

##  How to Run the Project

### 1.  Clone the Repository

```bash

cd linkedin-profile-analyzer
```

### 2.  Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate 
venv\Scripts\activate     
```

### 3.  Install Required Libraries

```bash
pip install -r requirements.txt
```

If you're using OpenAI API, create a `.env` file and add:

```
OPENAI_API_KEY=your_openai_key_here
```

### 4.  Run the Django Server

```bash
python manage.py runserver
```

Then open your browser and visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  Usage Instructions

###  Step 1: Launch the Application

After running the server, go to:

```
http://127.0.0.1:8000/
```

---

###  Step 2: Input LinkedIn Profile Sections

You’ll see a form where you can manually paste:

1. **Headline** – Your LinkedIn headline.
2. **Skills** – List of skills (comma-separated).
3. **About Section** – Your About/Bio section.

Then click **Analyze**.

---

###  Step 3: Review the Analysis

The app will process your input using AI/NLP and return:

-Grammar suggestions (from `language_tool_python`)
-Tone/Sentiment analysis (via `TextBlob` and `VADER`)
 Relevance insights (via `transformers` or `OpenAI`)

---

###  Step 4: Improve Profile Content

Use the feedback to:

- Fix grammar and sentence clarity
- Make your tone more professional or aligned with your target audience
- Improve relevance to your desired career field



##  Project Structure

```
linkedin_profile_analyzer/
│
├── analyzer/                  # Django app
│   ├── templates/
│   ├── views.py
│   ├── forms.py
│   └── utils/                 # NLP/AI logic here
│
├── linkedin_profile_analyzer/ # Django core settings
├── requirements.txt
├── manage.py
└── README.md
```
