class InsightAgentLite:
    """Simple multi-role agent skeleton."""

    def __init__(self):
        # In-memory cache for previous Q&A
        self.memory = {}

    def _search_memory(self, question: str):
        return self.memory.get(question)

    def _store_memory(self, question: str, answer: str):
        self.memory[question] = answer

    def orchestrate(self, question: str) -> str:
        """Plan tool usage. Placeholder implementation."""
        # In a real system, this would use an LLM to create a plan.
        plan = ["search_web", "search_stock"]
        return f"Planned steps: {', '.join(plan)}"

    def reason(self, gathered_info: str) -> str:
        """Generate final answer. Placeholder implementation."""
        # In a real system, this would run a second LLM pass.
        return f"\nBased on gathered info:\n{gathered_info}\n\n(analysis...)"

    def answer(self, question: str) -> str:
        cached = self._search_memory(question)
        if cached:
            return cached

        plan = self.orchestrate(question)
        # Placeholder tool execution
        gathered_info = f"Executed: {plan}"
        answer = self.reason(gathered_info)
        self._store_memory(question, answer)
        return answer
