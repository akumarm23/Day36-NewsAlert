import smtplib
import requests

# Constants and Configuration
MY_EMAIL = "pytestakm23@gmail.com"
PASSWORD = "iir(+p3GED5B"
APP_PASS = "wbenczbguvopkept"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "7c378abee02b4b5baa37f7a490a2676a"

# Function to fetch news articles
def fetch_news():
    news_params = {
        "apiKey": API_KEY,
        "q": "apple",
        "from": "2023-12-15",
        "to": "2023-12-15",
        "sortBy": "popularity",
    }

    news = requests.get(NEWS_ENDPOINT, params=news_params)
    news.raise_for_status()  # Raise an error for bad responses
    return news.json()["articles"][:5]

# Function to send emails
def send_email(headline, brief):
    connection = smtplib.SMTP("smtp.gmail.com", port=587, timeout=10)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=APP_PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:{headline}\n\n{brief}".encode('utf-8')
    )
    connection.close()

# Main Script
try:
    articles = fetch_news()

    output = [f"Headline: {article['title']}. Brief: {article['description']}" for article in articles]

    for news_article in output:
        brief_start = news_article.find("Brief:")
        headline = news_article[len("Headline:"):brief_start].strip()
        brief = news_article[brief_start + len("Brief:"):].strip()

        send_email(headline, brief)

    print("Script execution completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
