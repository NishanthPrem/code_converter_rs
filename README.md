# Python to Rust Code Converter

A web application that converts Python code to Rust code in real-time using Ollama's CodeLlama model, with the ability to execute both Python and Rust code directly in the interface.

## Features

- Real-time conversion of Python code to Rust
- Live code execution for both Python and Rust
- Web-based interface built with Gradio
- Streaming responses from the CodeLlama model
- Error handling for code compilation and execution

## Prerequisites

- Python 3.x
- Rust compiler (rustc)
- Ollama installed and running locally
- CodeLlama 7B model downloaded in Ollama

## Required Python Packages

```
ollama
gradio
python-dotenv
requests
IPython
```

## Installation

1. Clone the repository
2. Install the required Python packages:
   ```bash
   pip install ollama gradio python-dotenv requests IPython
   ```
3. Ensure Ollama is installed and running:
   ```bash
   # Start Ollama service
   ollama serve
   
   # Pull the CodeLlama model
   ollama pull codellama:7b
   ```

## Configuration

The application uses the following default settings:
- Ollama API endpoint: `http://localhost:11434/api/chat`
- Model: `codellama:7b`

## Usage

1. Start the application:
   ```bash
   python main.py
   ```

2. The web interface will automatically open in your default browser
3. Enter Python code in the left text box
4. Click "Convert code" to generate equivalent Rust code
5. Use the "Run Python" and "Run Rust" buttons to execute the respective code
6. View the execution results in the output areas below

## Architecture

The application consists of several key components:

- **Code Conversion**: Uses the CodeLlama model through Ollama API for Python to Rust translation
- **Code Execution**: 
  - Python code is executed using Python's built-in `exec()` function
  - Rust code is compiled with `rustc` and executed as a binary
- **Frontend**: Gradio-based web interface with real-time updates

## Error Handling

- Python execution errors are captured and displayed in the output area
- Rust compilation and runtime errors are caught and displayed with detailed error messages

## Limitations

- The code conversion quality depends on the CodeLlama model's capabilities
- Only console output is captured from code execution
- Complex Python programs might not convert perfectly to Rust
- Requires local installation of Rust compiler

## Security Notes

- Code execution is performed locally on your machine
- Be cautious when running unknown code
- No sandboxing is implemented by default
