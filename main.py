# Importing the libraries

import os
import io
import sys
import json
import requests
from dotenv import load_dotenv
import ollama
from IPython.display import Markdown, display, update_display
import gradio as gr
import subprocess

# Setting the constants

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = 'codellama:7b'

# Setting the prompts

system_message = "You are an assistant that reimplements Python code in Rust code."
system_message += "Respond only with Rust code and don't give me any explainations."

def user_prompt_for(python):
    user_prompt = "Rewrite this Python code in Rust"
    user_prompt += "Respond only with Rust code. Do not explain. Add all the required imports and main function"
    user_prompt += python
    return user_prompt

def messages_for(python):
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt_for(python)}
    ]

def stream(python):
    # Stream response for Ollama
    full_response = ""
    for chunk in ollama.chat(
        model=MODEL, 
        messages=messages_for(python),
        stream=True
    ):
        if 'message' in chunk and 'content' in chunk['message']:
            content = chunk['message']['content']
            full_response += content
            yield full_response.replace('```\n','').replace('```','')

def execute_python(code):
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
    finally:
        sys.stdout = sys.__stdout__
    return output.getvalue()

def execute_rust(code):
    # Step 1: Write the Rust code to a file
    rust_file = "main.rs"
    with open(rust_file, "w") as f:
        f.write(code)
    
    try:
        # Step 2: Compile the Rust code using rustc
        compile_result = subprocess.run(["rustc", rust_file], check=True, text=True, capture_output=True)
        
        # Step 3: Execute the compiled binary
        run_cmd = ["./main"]  # The default output binary name is "main" (or "main.exe" on Windows)
        run_result = subprocess.run(run_cmd, check=True, text=True, capture_output=True)
        
        # Step 4: Return the output of the executed binary
        return run_result.stdout
    
    except subprocess.CalledProcessError as e:
        # Handle compilation or runtime errors
        return f"An error occurred:\n{e.stderr}"

# Setting Up Gradio for the frontend

with gr.Blocks() as ui:
    gr.Markdown("## Convert code from Python to Rust")
    with gr.Row():
        python = gr.Textbox(label="Python code:", lines=10)
        rs = gr.Textbox(label="Rust:", lines=10)
    with gr.Row():
        convert = gr.Button("Convert code")
    with gr.Row():
        python_run = gr.Button("Run Python")
        rs_run = gr.Button("Run Rust")
    with gr.Row():
        python_out = gr.TextArea(label="Python result:", elem_classes=["python"])
        rs_out = gr.TextArea(label="Rust result:", elem_classes=["rs"])

    convert.click(stream, inputs=[python], outputs=[rs])
    python_run.click(execute_python, inputs=[python], outputs=[python_out])
    rs_run.click(execute_rust, inputs=[rs], outputs=[rs_out])

ui.launch(inbrowser=True)