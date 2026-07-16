!pip install -q google-genai gradio

from google import genai
import gradio as gr

# Replace with your Gemini API key
client = genai.Client(api_key="AQ.Ab8RN6J3eXMAMfdyEI3emhAYyIkHGpHR0O5d0b_pVTLe3wXg4g")


def convert_code(source_language, target_language, code):
    prompt = f"""
You are an expert programming language translator.

Convert the following {source_language} code into {target_language}.

Requirements:
- Preserve the original logic exactly.
- Use proper syntax and best coding practices.
- Add comments where necessary.
- Ensure the code is complete and executable.
- Return only the converted code.

{source_language} Code:
{code}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.Interface(
    fn=convert_code,
    inputs=[
        gr.Dropdown(
            choices=["Python", "Java", "C", "C++", "JavaScript", "C#", "Go", "PHP"],
            label="Source Language",
            value="Python"
        ),
        gr.Dropdown(
            choices=["Python", "Java", "C", "C++", "JavaScript", "C#", "Go", "PHP"],
            label="Target Language",
            value="Java"
        ),
        gr.Textbox(
            lines=20,
            placeholder="Paste your source code here...",
            label="Source Code"
        )
    ],
    outputs=gr.Textbox(
        lines=20,
        label="Converted Code"
    ),
    title="💻 AI Programming Language Converter",
    description="Convert source code from one programming language to another using Google's Gemini AI.",
    theme=gr.themes.Soft()
)

demo.launch()
