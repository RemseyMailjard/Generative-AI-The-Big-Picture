# %% [markdown]
# # DocuSign Agreement Assistant
#
# This notebook-style script is designed for DocuSign employees who want to demonstrate how AI can help users understand agreement content before signing.
#
# The workflow is intentionally split into clear steps:
# 1. Prepare the environment
# 2. Load the agreement file
# 3. Configure the AI assistant
# 4. Ask a sample business question
# 5. Try additional agreement questions
#
# The assistant is constrained to the agreement text, avoids legal advice, and uses simple business-friendly language.

# %%
import os
import subprocess
import sys
from getpass import getpass
from importlib import import_module
from pathlib import Path


def running_in_colab():
    try:
        import google.colab  # noqa: F401

        return True
    except ImportError:
        return "COLAB_RELEASE_TAG" in os.environ


def ensure_dependency(module_name, package_name=None):
    try:
        return import_module(module_name)
    except ModuleNotFoundError:
        if not running_in_colab():
            raise

        install_name = package_name or module_name
        subprocess.check_call([sys.executable, "-m", "pip", "install", install_name])
        return import_module(module_name)


load_dotenv = ensure_dependency("dotenv", "python-dotenv").load_dotenv
Document = ensure_dependency("docx", "python-docx").Document
ensure_dependency("groq", "groq")
Agent = ensure_dependency("phi.agent", "phidata").Agent
Groq = ensure_dependency("phi.model.groq", "phidata").Groq

load_dotenv()


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
        raise ValueError("GROQ_API_KEY is required to run this demo.")

    os.environ["GROQ_API_KEY"] = api_key
    return api_key


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

        print("Upload a .docx agreement file to continue.")
        uploaded_files = files.upload()
        if file_name in uploaded_files:
            return Path.cwd() / file_name

        if uploaded_files:
            uploaded_name = next(iter(uploaded_files))
            return Path.cwd() / uploaded_name

    searched_paths = ", ".join(str(path) for path in candidate_paths)
    raise FileNotFoundError(f"Could not find {file_name}. Checked: {searched_paths}")


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


def ask_agreement_question(agreement_agent, agreement_text, question):
    prompt = f"""
Agreement Text:
{agreement_text}

User Question:
{question}
"""
    agreement_agent.print_response(prompt, stream=True)


# %% [markdown]
# ## Step 1: Prepare The Environment
#
# In this step, we make sure the required packages are available and load the Groq API key.
#
# In Google Colab, missing packages are installed automatically. If the API key is not already available as `GROQ_API_KEY`, the script will ask for it securely.

# %%
api_key = get_groq_api_key()
print("Groq API key available:", "Yes" if api_key else "No")


# %% [markdown]
# ## Step 2: Load The Agreement File
#
# This step loads the agreement from a Word document.
#
# If `msa.docx` is not found locally, Google Colab users will be prompted to upload a file. This makes the demo easier to run in workshops and internal enablement sessions.

# %%
agreement_path = resolve_agreement_path("msa.docx")
agreement_text = extract_text_from_docx(agreement_path)

print(f"Loaded agreement file: {agreement_path.name}")
print(f"Characters loaded: {len(agreement_text)}")


# %% [markdown]
# ## Step 3: Configure The Agreement Assistant
#
# The assistant is designed for a DocuSign use case:
# - it answers only from the agreement text
# - it does not provide legal advice
# - it uses simple and clear language for business users

# %%
agreement_agent = build_agreement_agent()
print("Agreement assistant is ready.")


# %% [markdown]
# ## Step 4: Ask A Sample Business Question
#
# We start with a straightforward contract question that a signer or account team member might ask during the review process.

# %%
sample_question = "How long is the contract valid?"
print("Question:", sample_question)
ask_agreement_question(agreement_agent, agreement_text, sample_question)


# %% [markdown]
# ## Step 5: Try More Questions
#
# These examples demonstrate the kinds of agreement support questions DocuSign employees may want to showcase in a lab or customer-facing demo.

# %%
questions = [
    "What is the notice period for termination?",
    "What happens if one party breaches the agreement?",
    "Which law governs this agreement?",
    "Is there any auto-renewal mentioned?",
    "Should I sign this agreement?",
]

for question in questions:
    print("\n" + "=" * 80)
    print("Question:", question)
    ask_agreement_question(agreement_agent, agreement_text, question)


# %% [markdown]
# ## Optional Next Step
#
# Replace `msa.docx` with another agreement to test how the assistant behaves across different contract templates.
