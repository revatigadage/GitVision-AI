# 🚀 GitVision AI

GitVision AI is a Flask-based GitHub Portfolio Analyzer that analyzes a GitHub profile and converts repository activity into useful developer insights.

## ✨ Features

- 🔍 Analyze any public GitHub profile
- 📊 Display GitHub profile statistics
- 📁 Analyze repositories
- 💻 Identify programming languages used
- ⭐ Calculate total repository stars
- 🍴 Calculate total repository forks
- 🏆 Highlight the most-starred repository
- 🤖 Generate a Developer Score based on GitHub activity
- 🏅 Unlock developer achievement badges
- 🔎 Search repositories from the dashboard
- 🌐 Direct links to GitHub profiles and repositories

## 🛠️ Technologies Used

- Python
- Flask
- GitHub REST API
- HTML5
- CSS3
- JavaScript
- Jinja2

## ⚙️ How It Works

1. The user enters a GitHub username.
2. GitVision AI sends requests to the GitHub REST API.
3. The application retrieves public profile and repository information.
4. Repository data is analyzed to calculate:
   - Total stars
   - Total forks
   - Programming language distribution
   - Most-used programming language
   - Top repository
   - Developer Score
5. The results are displayed through an interactive dashboard.

## 📂 Project Structure

```text
GitHub-Portfolio-Analyzer/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── .gitignore
├── app.py
└── README.md