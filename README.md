# RAG Chatbot for Literature Review
A powerful Retrieval Augmented Generation (RAG) system that combines OpenAI's LLM capabilities with LangChain for efficient academic literature processing and analysis. This project was developed as part of an application process with approximately 5 hours of development time.

## Overview
This chatbot processes and analyzes academic literature focused on Human-AI interaction research papers, but can be applied to all text-based documents. The system combines semantic search capabilities with text generation to enable complex answers based on individual knowledge bases.

## Features

Paper Analysis Capabilities:
- Contextual extraction and summarization
- Research question and findings identification 
- Thematic analysis (Human vs. AI, Human-AI Collaboration)
- Methodological classification
- Contribution assessment
- Future research direction identification


Interactive Query System:
- Natural language query processing with semantic understanding
- Real-time literature review generation
- Dynamic paper retrieval and synthesis
- Academic citation formatting

## Installation
Just open the jupyter notebook in Google Colab through the provided button and run all cells.

## Usage
The implementation provides an interactive chatbot user interface for ease of use.
![Chatbot Interface](https://raw.githubusercontent.com/trashpanda-ai/RAG-chatbot/main/example.png)

Example queries:
- "Show me all empirical studies on human-AI collaboration"
- "Please summarize Gnewuch et al. 2023"

## Prompt Guidance
For paper summaries, the system extracts:
1. Context
2. Research Question and Findings
3. Theme of Research (Human vs. AI or Human + AI Collaboration)
4. Method (Conceptual/Case Study, Modeling, or Empirical Study)
5. Contribution
6. Future Potential and Limitations

For literature reviews, the system:
1. Retrieves relevant articles from the database
2. Generates formatted summaries
3. Compiles coherent thematic paragraphs
4. Provides academic citations
   
### Outlook: incoming features and improvements
- Add tabular database for all summaries (to reduce API calls and make questions on counts more reliable)
- Improve guidance prompts for RAG 
- Enhance user interface
