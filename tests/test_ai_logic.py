
def format_prompts(query):
    return f"Here's a chill take on: {query}", f"Formal explanation of: {query}"

def test_prompt_formatting():
    query = "Explain AI"
    casual, formal = format_prompts(query)
    assert query in casual
    assert query in formal