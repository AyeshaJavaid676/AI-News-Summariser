import gradio as gr
from summariser import summarize_text

def generate_summary(news_text):
    """
    Gradio wrapper for summarizing news text.
    
    Args:
        news_text (str): Full news article text.
        
    Returns:
        tuple: (summary, category) displayed in two separate textboxes.
    """
    result = summarize_text(news_text)
    
    if "error" in result:
        return result["error"], "Error"

    summary_text = f"📌 **Key Takeaways & Summary:**\n{result['summary']}"
    category_text = f"📰 **Category:** {result['category']}"

    return summary_text, category_text

# Gradio UI with two separate output textboxes
interface = gr.Interface(
    fn=generate_summary,
    inputs=gr.Textbox(lines=10, placeholder="Paste news article text here..."),
    outputs=[
        gr.Textbox(label="News Summary & Key Takeaways", lines=10), 
        gr.Textbox(label="News Category", lines=2)
    ],
    title="🧠 AI-Powered News Summarizer",
    description="Enter a news article, and AI will summarize it for you."
)

# Run Gradio app
if __name__ == "__main__":
    interface.launch(share=True)
