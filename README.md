# AI Code Generator

An AI-powered code generation web application that converts natural language descriptions into executable code snippets using **Python**, **Flask**, and **NLP**. The project allows users to input simple queries and get code snippets in various programming languages.

## Technologies & Tools Used

- **Python**: The primary programming language for backend development, responsible for handling the core logic and processing.
- **Flask**: A lightweight web framework used to build the web application, facilitating the creation of APIs and handling HTTP requests.
- **HTML/CSS/JavaScript**: Technologies employed for frontend development, creating the user interface and ensuring interactivity.
- **Natural Language Processing (NLP)**: Used for processing and understanding natural language inputs, enabling the generation of code based on user queries.

## Project Structure

- **`code_generator/`**: Contains modules responsible for generating code snippets based on user input.
- **`compiler/`**: Handles the compilation and execution of generated code snippets.
- **`compiler_ui/`**: Provides the user interface for interacting with the compiler module.
- **`nlp_processing/`**: Includes components for processing and interpreting natural language inputs.
- **`main.py`**: The main entry point for the application, initializing and running the Flask server.
- **`server.py`**: Manages server-side logic and routes for handling requests.
- **`index.html`**: The main HTML file for the frontend interface.
- **`style.css`**: Defines the styling and layout of the frontend interface.
- **`script.js`**: Contains JavaScript code for frontend interactivity and asynchronous operations.

## Key Features

- **Code Generation**: Converts natural language descriptions into functional code snippets across various programming languages.
- **Code Compilation**: Compiles and executes generated code snippets, providing real-time feedback to users.
- **User Interface**: A web-based interface that allows users to input natural language queries and view generated code and execution results.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/harshitp1603/AI-Code-Generator2.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python main.py
4. Access the application in your browser at http://localhost:5000.
