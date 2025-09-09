#import _typeshed
import os
import sys
from google.genai import types

import argparse
parser = argparse.ArgumentParser(description='a sample script')
parser.add_argument('--verbose', action='store_true', help='Enable verbose')
parser.add_argument('prompt', type=str)
args = parser.parse_args()

from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
client = genai.Client(api_key=api_key)

def main():
    if len(args.prompt) < 2:
        print("No prompt provided")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]
    response = client.models.generate_content(
	model='gemini-2.0-flash-001', contents=messages,
	)

    print("Hello from aiagent!")
    print(response.text)
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
