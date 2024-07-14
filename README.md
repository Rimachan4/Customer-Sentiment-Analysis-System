# Customer-Sentiment-Analysis-System

## Overview
This system analyzes customer reviews to determine sentiment (positive or negative) and generates appropriate response emails using a Language Model (LLM). It reads reviews from a JSON file (`reviews.json`), processes them, and drafts emails based on predefined instructions.

## Features
- **Sentiment Analysis**: Automatically detects whether a review is positive or negative.
- **Email Generation**: Generates response emails based on the sentiment:
  - **Positive Review**: Sends a thank-you email to the customer and recommends a new product.
  - **Negative Review**: Sends an apology email to the customer and notifies a senior customer service representative internally.

## Implementation Steps
1. **Input Handling**:
   - Reads customer reviews from `reviews.json`.
   - Stores reviews in a structured format (JSON array of dictionaries).

2. **Sentiment Analysis**:
   - Utilizes a Language Model (LLM) to determine sentiment:
     - **Positive**: Generates a thank-you email and recommends a new product.
     - **Negative**: Generates an apology email and notifies internally.

3. **Email Drafting**:
   - Uses LLM to draft emails based on the sentiment analysis results.
   - Products for recommendations are read from `products.json` (currently selected randomly).

4. **Run the Application**:
   - Execute the Streamlit application (streamlit run Task2.py).
   - The application will load reviews, perform sentiment analysis using LLM, and generate emails based on the reviews.

## Setup
- **Environment**: Ensure all necessary dependencies are installed (`streamlit`, `dotenv`, `langchain_google_genai`, etc.).
- **Configuration**: Store sensitive information (API keys, etc.) in a `.env` file and load them using `dotenv`.

