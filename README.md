# Python to Rust Converter

A simple web application that allows you to convert Python code to Rust code and execute both to compare results.

## Features

- Convert Python code to Rust code using the Codellama model
- Execute Python code directly within the application
- Compile and run Rust code to see the results
- Clean, intuitive interface built with Gradio

## Prerequisites

- Python 3.7+
- Rust compiler (rustc) installed and in your PATH
- Ollama running locally with the Codellama model available

## Installation with uv

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-to-rust-converter.git
   cd python-to-rust-converter
   ```

2. Create a virtual environment and install dependencies with uv:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages with uv add:
   ```bash
   uv add ollama gradio
   ```

## Usage

1. Make sure Ollama is running with the Codellama model:
   ```bash
   ollama run codellama
   ```

2. Run the application:
   ```bash
   uv run main.py
   ```

3. Open your browser at the URL displayed in the terminal (usually http://127.0.0.1:7860)

4. Enter your Python code in the left textbox and click "Convert code" to generate the Rust equivalent

5. Use the "Run Python" and "Run Rust" buttons to execute each version and compare outputs

## How It Works

1. The application uses Ollama's API to access the Codellama model for Python to Rust conversion
2. Python code is executed directly using Python's `exec()` function
3. Rust code is written to a temporary file, compiled with `rustc`, and then executed
4. Results from both executions are displayed for comparison

## Configuration

- Default Ollama API endpoint: `http://localhost:11434/api/chat`
- Default model: `codellama`

You can modify these settings in the code if needed.

## Troubleshooting

- Ensure Ollama is running and accessible at the configured API endpoint
- Verify that the Codellama model is available in your Ollama installation
- Make sure Rust is properly installed and `rustc` is in your PATH
- Check that you have permissions to create and execute files in the directory

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.