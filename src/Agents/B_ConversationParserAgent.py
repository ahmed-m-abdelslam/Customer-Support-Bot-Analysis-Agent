from Schema.conversation import Turn

class ConversationParserAgent:
    def run(self, raw_text: str):
        chunks = raw_text.split(":::")
        turns = []

        for i, chunk in enumerate(chunks):
            chunk = chunk.strip()

            if chunk.startswith("User:"):
                speaker = "User"
                message = chunk.replace("User:", "").strip()
            elif chunk.startswith("Agent:"):
                speaker = "Agent"
                message = chunk.replace("Agent:", "").strip()
            else:
                continue

            turns.append(Turn(
                speaker=speaker,
                message=message,
                position=i
            ))

        return turns
