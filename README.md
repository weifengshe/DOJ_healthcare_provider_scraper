# DOJ Healthcare Provider Analysis

This project scrapes DOJ press releases and analyzes them for healthcare provider mentions using OpenAI's GPT-3.5.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
- Copy `.env.example` to `.env`
- Add your OpenAI API key to `.env`

## Usage

Run the script:
```bash
python main.py
```