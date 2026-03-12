import os
from getpass import getpass
from pathlib import Path

from dotenv import load_dotenv
from docx import Document
from phi.agent import Agent
from phi.model.groq import Groq

load_dotenv()


def running_in_colab():
    try:
        import google.colab  # noqa: F401

        return True
    except ImportError:
        return "COLAB_RELEASE_TAG" in os.environ


def get_groq_api_key():
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        return api_key

    if running_in_colab():
        try:
            from google.colab import userdata

            api_key = userdata.get("GROQ_API_KEY")
            if api_key:
                os.environ["GROQ_API_KEY"] = api_key
                return api_key
        except Exception:
            pass

    api_key = getpass("Enter your GROQ_API_KEY: ").strip()
    if not api_key:
        raise ValueError("GROQ_API_KEY is required to run this script.")

    os.environ["GROQ_API_KEY"] = api_key
    return api_key


def build_agreement_agent():
    get_groq_api_key()
    return Agent(
        name="DocuSign Agreement Assistant",
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=[
            "You are an AI assistant for an electronic agreement platform.",
            "Answer only from the provided agreement text.",
            "If information is missing, say: Not mentioned in the agreement.",
            "Do not provide legal advice.",
            "Use simple and clear language.",
        ],
        markdown=False,
    )


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())

    return "\n".join(text)


def resolve_agreement_path(file_name="msa.docx"):
    candidate_paths = [Path.cwd() / file_name]

    if "__file__" in globals():
        candidate_paths.insert(0, Path(__file__).resolve().parent / file_name)

    for candidate in candidate_paths:
        if candidate.exists():
            return candidate

    if running_in_colab():
        from google.colab import files

        uploaded_files = files.upload()
        if file_name in uploaded_files:
            return Path.cwd() / file_name

        if uploaded_files:
            uploaded_name = next(iter(uploaded_files))
            return Path.cwd() / uploaded_name

    searched_paths = ", ".join(str(path) for path in candidate_paths)
    raise FileNotFoundError(f"Could not find {file_name}. Checked: {searched_paths}")


def main():
    agreement_path = resolve_agreement_path()
    agreement_text = extract_text_from_docx(agreement_path)
    agreement_agent = build_agreement_agent()

    agreement_agent.print_response(
        f"""
Agreement Text:
{agreement_text}

User Question:
How long is the contract valid?
""",
        stream=True,
    )


if __name__ == "__main__":
    main()

# questions = [
#     "What is the notice period for termination?",
#     "What happens if one party breaches the agreement?",
#     "Which law governs this agreement?",
#     "Is there any auto-renewal mentioned?",
#     "Should I sign this agreement?"
# ]

# for q in questions:
#     agreement_agent.print_response(
#         f"Agreement Text:\n{agreement_text}\n\nQuestion:\n{q}",
#         stream=True
#     )
