import os
import groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Client
client = groq.Client(api_key=GROQ_API_KEY)

def summarize_text(text):
    """
    Summarizes a given news article text using Groq API.

    Args:
        text (str): The full news article text.

    Returns:
        dict: A dictionary containing key takeaways, a summary, and a category.
    """

    prompt = f"""
    Read the following news article and perform the following tasks:
    
    1. **Summarize the article in 3-5 concise sentences.**
    2. **Extract the key takeaways in bullet points.**
    3. **Classify the news into a category from the following list:**
       - Politics, Business, Sports, Science, Technology, Health, Entertainment, Environment, or World News.

    **Article:**
    {text}

    **Format the response exactly like this:**
    - Summary: [Your summary here]
    - Key Takeaways: 
      1. [Takeaway 1]
      2. [Takeaway 2]
      3. [Takeaway 3]
    - Category: [One of Politics, Business, Sports, Science, Technology, Health, Entertainment, Environment, World News]
    """

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Ensure you are using a valid Groq model
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = response.choices[0].message.content

        # Extract summary, key takeaways, and category
        summary = response_text.split("- Summary: ")[1].split("- Key Takeaways:")[0].strip()
        key_takeaways = "- Key Takeaways:" + response_text.split("- Key Takeaways:")[1].split("- Category:")[0].strip()
        category = response_text.split("- Category:")[1].strip()

        return {
            "category": category, 
            "summary": f"**Summary:** {summary}\n\n{key_takeaways}"
        }

    except Exception as e:
        return {"error": f"Failed to fetch summary: {str(e)}"}
