def parse_conversation(raw_text: str):
    turns = []
    chunks = raw_text.split(":::")

    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()

        if chunk.startswith("User:"):
            turns.append({
                "speaker": "User",
                "message": chunk.replace("User:", "").strip(),
                "position": i
            })
        elif chunk.startswith("Agent:"):
            turns.append({
                "speaker": "Agent",
                "message": chunk.replace("Agent:", "").strip(),
                "position": i
            })

    return turns
