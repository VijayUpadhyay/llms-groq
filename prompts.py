import os
from typing import List, Dict

from llama_index.core import PromptTemplate
from llama_index.llms.groq import Groq

os.environ["GROQ_API_KEY"] = ""




def run_llm_fewshot(context: str, query: str, examples: List[Dict[str, str]]) -> str:
    llm = Groq(model="llama-3.3-70b-versatile", temperature=0)

    examples_str = "\n".join(
        f"Example {i+1}:\nContext:\n{ex.get('context','')}\n"
        f"Question: {ex.get('question','')}\n"
        f"Answer: {ex.get('answer','')}\n"
        for i, ex in enumerate(examples)
    )

    template_str = (
        "You are an expert AI assistant.\n"
        "Use ONLY the provided context to answer the user's question. "
        "If the context is insufficient or does not mention the answer, reply exactly: "
        "'Not enough information.'\n\n"
        "Follow the style and reasoning illustrated by the examples.\n\n"
        "Examples:\n{examples_str}\n"
        "--- End of Examples ---\n\n"
        "Context:\n{context_str}\n\n"
        "User Question: {query_str}\n\n"
        "Answering Rules:\n"
        "1) Be concise and precise (3–6 sentences, unless the question requires more).\n"
        "2) Use bullet points for lists.\n"
        "3) At the end, include a 'Sources:' section with short snippets or filenames from the context you used.\n\n"
        "Final Answer:"
    )
    prompt_details = PromptTemplate(template_str).format(
        examples_str=examples_str, context_str=context, query_str=query
    )
    return llm.complete(prompt=prompt_details).text
