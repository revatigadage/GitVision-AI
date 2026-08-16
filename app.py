from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    username = request.form["username"].strip()

    # Profile API
    profile_url = f"https://api.github.com/users/{username}"

    try:
        profile_response = requests.get(profile_url, timeout=10)
    except requests.exceptions.RequestException:
        return render_template(
            "index.html",
            error="❌ Unable to connect to GitHub. Please try again later."
        )

    data = profile_response.json()

    if profile_response.status_code != 200:
        return render_template(
            "index.html",
            error="❌ GitHub user not found. Please enter a valid username."
        )

    # Repository API
    repo_url = f"https://api.github.com/users/{username}/repos"

    try:
        repo_response = requests.get(repo_url, timeout=10)
    except requests.exceptions.RequestException:
        return render_template(
            "index.html",
            error="❌ Unable to connect to GitHub. Please try again later."
        )

    repos = repo_response.json()

    if not isinstance(repos, list):
        repos = []

    repos.sort(
        key=lambda repo: repo.get("stargazers_count", 0),
        reverse=True
    )
    # Count programming languages
    languages = {}

    for repo in repos:

        language = repo.get("language")

        if language:

            languages[language] = languages.get(language, 0) + 1

        # Calculate total stars and forks
    total_stars = 0
    total_forks = 0

    for repo in repos:
        total_stars += repo.get("stargazers_count", 0)
        total_forks += repo.get("forks_count", 0)

    # Find the most used language
    most_used_language = "Not Available"

    if languages:
        most_used_language = max(languages, key=languages.get)
        # Find repository with highest stars
    top_repo = None

    if repos:
        top_repo = max(repos, key=lambda repo: repo.get("stargazers_count", 0))

        # Calculate Developer Score
    developer_score = min(
    100,
    (
        data["public_repos"] * 2
        + total_stars
        + total_forks
        + len(languages) * 5
        + data["followers"] // 2
    )
)
    # Achievement Badges
    achievements = []

    if total_stars >= 100:
        achievements.append("⭐ Popular Developer")

    if len(languages) >= 3:
        achievements.append("💻 Polyglot Programmer")

    if data["public_repos"] >= 20:
        achievements.append("📁 Repository Master")

    if total_forks >= 50:
        achievements.append("🔥 Open Source Contributor")

    if developer_score >= 80:
        achievements.append("🌟 Rising Developer")

    repos.sort(
    key=lambda repo: repo.get("stargazers_count", 0),
    reverse=True
    )

    top_repositories = repos[:6]
    

    return render_template(
        "result.html",
        data=data,
        repos=top_repositories,
        languages=languages,
        top_repo=top_repo,
        total_stars=total_stars,
        total_forks=total_forks,
        most_used_language=most_used_language,
        developer_score=developer_score,
        achievements=achievements
    )


if __name__ == "__main__":
    app.run(debug=True)



    