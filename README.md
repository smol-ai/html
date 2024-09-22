# AI Chat History

## Description

AI Chat History is a web application that allows users to interact with an AI assistant and view their chat history. The project is built using Next.js, React, and Tailwind CSS for the frontend, with a Python backend for AI integration.

## Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (v14 or later)
- npm (v6 or later)
- Python (v3.8 or later)
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ai-chat-history.git
   cd ai-chat-history
   ```

2. Install frontend dependencies:
   ```
   npm install
   ```

3. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env.local` file in the root directory and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### First-time setup

1. Start the development server:
   ```
   npm run dev
   ```

2. In a separate terminal, start the Python backend:
   ```
   python backend/main.py
   ```

3. Open your browser and navigate to `http://localhost:3000`

### Subsequent runs

1. Start the development server:
   ```
   npm run dev
   ```

2. Start the Python backend:
   ```
   python backend/main.py
   ```

3. Open your browser and navigate to `http://localhost:3000`

## Project Structure

