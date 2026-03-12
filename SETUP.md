# Environment Setup

This guide helps you prepare your environment for the **Generative AI - The Big Picture** course. The setup supports the notebooks, markdown exercises, and optional project work included in this repository.

## Prerequisites

- Python 3.10 or higher
- A Groq account and API key for the hands-on notebooks and agent examples

Check your Python version:

```bash
python --version
```

If Python is not installed yet, download it from [python.org](https://www.python.org/). Try installing Python 3.14.3

## Optional: Install uv

`uv` is a fast Python package and environment manager. You can use it alongside the standard Python setup in this course.

Install `uv`:

**Mac / Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify that it works:

```bash
uv --version
```

## Step 1: Create a Groq Account and API Key

Create your Groq account first so you can use the notebooks and agent examples later without interruption.

- Go to https://console.groq.com/
- Sign up or log in
- Open the API Keys section
- Create a new API key

Create a `.env` file in the root of this project with:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Verify that the file exists:

**Windows:**
```powershell
Get-ChildItem .env
```

**Mac/Linux:**
```bash
ls -a .env
```

## Step 2: Open This Project Folder

Open a terminal in the root of this repository, the folder that contains `requirements.txt`, `NOTEBOOKS/`, `MARKDOWN/`, and `PROJECT WORK/`.

## Step 3: Create a Virtual Environment

Create a local virtual environment in the project folder:

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```powershell
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

## Step 4: Install Dependencies

First upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

Then install the project dependencies:

```bash
pip install -r requirements.txt
```

This installs the packages needed for:
- prompt engineering exercises
- Groq-based notebooks
- chatbot examples
- DocuSign and finance agent examples in `PROJECT WORK/`

## Step 5: Verify the Installation

Run these quick checks:

```bash
python -c "import groq; print('Groq OK')"
python -c "from phi.agent import Agent; print('Phidata OK')"
```

If you also want to use the retrieval examples, you can verify FAISS as well:

```bash
python -c "import faiss; print('FAISS OK')"
```

## Step 6: Register a Jupyter Kernel

Install and register the virtual environment as a notebook kernel:

```bash
pip install ipykernel
python -m ipykernel install --user --name genai-big-picture
```

Then select the `genai-big-picture` kernel when opening a notebook.

## What This Setup Covers

| Material | Folder |
|----------|--------|
| Course notes and background reading | `MARKDOWN/` |
| Hands-on notebooks | `NOTEBOOKS/` |
| Workshop notebook and agent examples | `PROJECT WORK/` |

## Running The Materials

Start Jupyter from the project root:

```bash
jupyter notebook
```

Recommended order:

1. Read the guides in `MARKDOWN/`
2. Open the notebooks in `NOTEBOOKS/`
3. Explore the optional examples in `PROJECT WORK/`

## Troubleshooting

**"No module named 'phi'"**

Install the correct package:

```bash
pip install phidata
```

**`inspect.getargspec` error**

This usually means a conflicting `phi` package is installed:

```bash
pip uninstall phi -y
pip install phidata
```

**Notebook cannot find installed packages**

Make sure the notebook is using the `genai-big-picture` kernel and that your virtual environment was activated when you installed the dependencies.
