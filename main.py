import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY") or RuntimeError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from AlexanderAI!")

    current_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=current_prompt
    )

    print("User prompt: ", current_prompt)

    if response.usage_metadata is not None:
      print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
      print("Response tokens: ", response.usage_metadata.candidates_token_count)
      print("Response: ", response.text)
    else:
      raise RuntimeError("Response usage metadata is None, cannot print token counts.")

if __name__ == "__main__":
    main()
