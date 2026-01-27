class EntryGatewayAgent:
    def run(self, record: dict):
        conversation_text = record["conversation"]

        return {
            "conversation_id": record.get("index"),
            "raw_text": conversation_text,
            "language": "ar" if any("ا" <= c <= "ي" for c in conversation_text) else "en",
            "length": conversation_text.count(":::") + 1
        }
