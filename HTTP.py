import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Define your target keywords
keywords = {
    "python": 0,
    "javascript": 0,
    "java": 0,
    "golang": 0,
    "rust": 0,
    "c++": 0,
    "typescript": 0,
    "ruby": 0
}

def scrape_comments(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Get elements with class "ind" and indent=0 (top-level comments)
    elements = soup.find_all("td", class_="ind", indent=False)
    comments = [e.find_next("span", class_="comment") for e in elements]

    # Extract and clean comment texts
    comment_texts = [comment.get_text() for comment in comments if comment]
    return comment_texts

def analyze_comments(comment_texts):
    # Flatten all comment texts into one set of words
    words = " ".join(comment_texts).lower().split()
    words = {w.strip(".,/:;!@") for w in words}

    for k in keywords:
        if k in words:
            keywords[k] += 1

def plot_keywords():
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.title("Programming Language Mentions in HN Comments")
    plt.show()

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    print(f"Scraping: {url}")

    comment_texts = scrape_comments(url)
    print(f"Found {len(comment_texts)} top-level comments")

    analyze_comments(comment_texts)
    print("Keyword scores:", keywords)

    plot_keywords()

if __name__ == "__main__":
    main()
