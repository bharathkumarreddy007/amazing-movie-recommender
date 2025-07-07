# 🎬 Amazing Movie Recommender

Welcome to the **Amazing Movie Recommender** — a personalized project built and customized by **A.V. Bharath Kumar Reddy** for portfolio use. This tool helps users discover movies similar to their favorites based on content similarity and real-time poster data from TMDB.

> _“Customized, modified, and deployed by Bharath as part of his Data Science learning journey.”_

---

## 💡 About This Project

This project was adapted and enhanced from open-source logic with meaningful improvements:
- Cleaned UI/UX using **Streamlit**
- Real-time movie posters with **TMDB API**
- Case-insensitive matching and error handling
- Added custom portfolio credits and .env security

🎯 Goal: Learn recommendation systems, Python tools, and API integration hands-on.

---

## 🚀 Try It Live

👉 [Amazing Movie Recommender – Deployed on Streamlit](https://your-deployed-app-link.streamlit.app)

> *(Replace the above link with your actual Streamlit app URL once deployed)*

---

## 📦 Tech Stack

- `Python`  
- `Pandas`, `Pickle`, `Requests`, `dotenv`  
- `Streamlit` (Web App Framework)  
- `TMDB API` for real movie posters

---

## 🧠 How It Works

1. The user selects a movie title from a dropdown list.
2. The app uses a **precomputed similarity matrix** to find the top similar movies.
3. Posters are fetched dynamically from **The Movie Database (TMDB)**.
4. If a movie isn't found, the app shows friendly feedback.

---

## 🖥️ Run It Locally

```bash
# Clone the project
git clone https://github.com/YOUR_USERNAME/netflix-recommender-app.git
cd netflix-recommender-app

# Optional: Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Add your TMDB API key to a `.env` file like:
# API_KEY=your_actual_tmdb_api_key

# Launch the app
streamlit run deploy.py
