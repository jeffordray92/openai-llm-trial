# Django Todo App with OpenAI Integration

This project is a Django-based Todo application that integrates with OpenAI to generate task instructions based on a provided title. The app uses GPT-3.5 or GPT-4 (if specified) to generate structured lists of steps for each todo item.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jeffordray92/openai-llm-trial.git
```

### 2. Create and Configure `.env` File

An `.env-sample` file is provided as a template for environment variables. Create a `.env` file from this sample and add your OpenAI API key along with other required settings.

```bash
cp .env-sample .env
```

In the `.env` file, set the following values:

```plaintext
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key

# Optional: Specify the OpenAI model to use (defaults to gpt-3.5-turbo if not set)
GPT_MODEL=gpt-3.5-turbo
```

### 3. Install Dependencies

Make sure you have Python and pip installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Migrate the Database

Run migrations to set up the database schema.

```bash
python manage.py migrate
```

### 5. Run the Development Server

To start the Django development server, run:

```bash
python manage.py runserver
```

The app should now be accessible at `http://127.0.0.1:8000/`.

## Notes

- The application defaults to `gpt-3.5-turbo` if `GPT_MODEL` is not specified in `.env`.
- Make sure your OpenAI API key has sufficient quota and permissions for the specified model.
