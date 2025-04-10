# Ask the Llama

This project is a Flask-based application integrated with the Ollama server Python framework.

## Project Structure

```
flask/
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── agents.yaml
│   ├── routes.py
├── static/
│   ├── css/
│   ├── img/
│   ├── js/
├── templates/
│   ├── index.html
├── run.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd flask
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Install the Ollama server Python framework:
```bash
pip install ollama
```

## Running the Application

1. Start the Flask server:
```bash
cd flask
python run.py
```

2. By default, the server will run at `http://localhost:9100`. You can specify a different host and port:
```bash
python run.py <host> <port> [-d]
```

   - `<host>`: The host address (default: `localhost`).
   - `<port>`: The port number (default: `9100`).
   - `-d`: Enable debug mode (optional).

## Usage

- Open your browser and navigate to the server's URL to interact with the application.
- The application uses the `agents.yaml` configuration file to manage system roles and models.

## Notes

- Ensure the `agents.yaml` file is properly configured for the application to function correctly.
- The Ollama server framework is required for the AI functionalities in the application.


