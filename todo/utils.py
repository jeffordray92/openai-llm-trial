import re

from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
GPT_MODEL = settings.GPT_MODEL


def is_bullet_list(text):
    bullet_pattern = r"^- .+"
    return all(re.match(bullet_pattern, line) for line in text.splitlines())


def generate_llm_response(title):
    system_message = "You are an assistant that provides step-by-step instructions in a specific format."
    user_message = f"""Provide a bulleted list of specific tasks to complete the following task: '{title}'.
Each task should begin with a hyphen followed by a description, as shown below:

- Gather cleaning supplies: vacuum, mop, duster, cleaning cloths, glass cleaner, and multi-surface cleaner.
- Remove any trash and take out the garbage.
- Collect and organize any clutter or misplaced items; put them in their correct spots.

Only respond in this format with each task starting with a hyphen and a space. The list should be comprehensive, but only limit to a maximum of 5 specific tasks.
"""

    completion = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
    )

    tasks = completion.choices[0].message.content.strip()

    if is_bullet_list(tasks):
        return '\n'.join(line.strip() for line in tasks.splitlines() if line.strip())
    else:
        return None