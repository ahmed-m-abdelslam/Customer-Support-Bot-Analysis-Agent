class ContextBuilderAgent:
    def run(self, turns):
        user_msgs = [t.message for t in turns if t.speaker == "User"]
        agent_msgs = [t.message for t in turns if t.speaker == "Agent"]

        summary = " ".join(user_msgs[-3:])  # آخر شكاوي غالبًا أهم

        stats = {
            "user_turns": len(user_msgs),
            "agent_turns": len(agent_msgs),
            "repetition": len(user_msgs) - len(set(user_msgs))
        }

        return {
            "user_messages": user_msgs,
            "agent_messages": agent_msgs,
            "summary": summary,
            "stats": stats
        }
