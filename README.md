# RAG Chatbot for Literature Review
A powerful Retrieval Augmented Generation (RAG) system designed for academic literature analysis. This tool combines OpenAI's language models with LangChain's document processing capabilities to assist in literature review tasks. The system processes academic documents and enables interactive conversations about their content, helping researchers extract and analyze information efficiently. Built as a proof of concept in approximately 5 hours (as part of an application process), this implementation demonstrates a straightforward approach to augmenting literature review workflows with AI assistance. The architecture prioritizes simplicity and ease of use. It maintains robust functionality for document processing and information retrieval to promote Human-AI collaboration.


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
Just open the Jupyter Notebook in Google Colab through the provided button and run all cells:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/trashpanda-ai/RAG-chatbot/blob/main/RAG_chatbot.ipynb)

## Usage
The implementation provides an interactive chatbot user interface for ease of use. (*Also, the text is easy to copy since it includes markdown formatting wihtout rendering it as such.*)
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


### Full Queries and Answers

Query: ```"Please summarize Gnewuch et al. 2023"```

Answer: 
```
1. **Context**: The study focuses on customer interactions with hybrid service agents, which combine human and AI elements in service delivery. It explores how these interactions affect customer satisfaction and service outcomes.

2. **Research Question & Summary of Key Findings**: The research investigates how the presence of AI in service interactions influences customer perceptions and behaviors. Key findings suggest that customers exhibit varying levels of trust and satisfaction based on the hybrid nature of the service agent. Specifically, the study identifies that customers prefer human agents for complex inquiries but appreciate AI for efficiency in straightforward tasks.

3. **Theme**: Human + AI Collaboration: The study emphasizes the roles of both human and AI agents in service interactions, highlighting how their collaboration can enhance customer experiences.

4. **Method**: Empirical Study: The research employs empirical methods, including surveys and experiments, to gather data on customer interactions with hybrid service agents.

5. **Contribution**: The study contributes to the understanding of hybrid service models by providing insights into customer preferences and the dynamics of human-AI collaboration in service contexts. It offers practical implications for businesses looking to optimize their service delivery through AI integration.

6. **Future Directions & Limitations**: The research identifies gaps in understanding the long-term effects of hybrid service agents on customer loyalty and the potential for AI to handle more complex tasks. Future studies could explore these dimensions further and address the limitations of current AI capabilities in service settings.

### References
- Gnewuch, U., et al. (2023) • Customer Interactions with Hybrid Service Agents. Information Systems Research, Articles in Advance. DOI: 10.1287/mnsc. 2023.4770.
```

Query: ```"Among the 32 papers, [XX] are conceptual studies, [XX] are modeling studies (either stylized or OR models), and [XX] are empirical studies. Of the empirical studies, [XX] are experiments, and [XX] use secondary data analysis. Please provide the exact count for each type of research."```

Answer:  
```
Based on the analysis of the 32 papers regarding human vs. AI research, the counts for each type of research are as follows:
- **Conceptual Studies**: 10
- **Modeling Studies**: 8
- **Empirical Studies**: 14
  - **Experiments**: 6
  - **Secondary Data Analysis**: 8
These counts provide a comprehensive overview of the research landscape in the context of human and AI interactions.
```


Query: ```"please summarise empirical research about human VS AI"```

Answer:
```
1. **Context**: The focus of this empirical research is on the dynamics of human-AI collaboration, particularly in knowledge work settings, and how different levels of worker experience influence the effectiveness of AI.

2. **Research Question & Summary of Key Findings**: The research investigates how work experience affects the productivity gains from AI in knowledge work. Key findings indicate that AI enhances productivity for all workers, but the benefits are more pronounced for those with greater task-based experience compared to those with more time-based experience. Senior workers, who have a broader scope of work and greater organizational concerns, tend to be more sensitive to AI's imperfections, leading to reduced trust and pushback against AI tools.

3. **Theme**: Human vs. AI: The study highlights the comparative advantages of human workers with different experience types in leveraging AI, showcasing scenarios where human sensitivity to AI limitations can hinder collaboration.

4. **Method**: Empirical Study: The research employs empirical analysis through a specific task-level examination, allowing for insights into individual worker factors that influence AI benefits.

5. **Contribution**: The study contributes to the understanding of human-AI teaming dynamics, providing empirical evidence of AI's positive impact on productivity in knowledge work. It offers practical implications for executives and policymakers to foster productive human-AI relationships.

6. **Future Directions & Limitations**: The research identifies gaps in understanding the nuances of human-AI interaction, particularly regarding the varying perceptions and trust levels among different worker demographics. Future studies could explore these dynamics further and address the limitations of existing AI tools in meeting expectations in various contexts.

### References
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence: Review of empirical research. Academy of Management Annals, 14(2), 627–660.
- Argo, J. J., & Dahl, W. D. (2020). Social influence in the retail context: A contemporary review of the literature. Journal of Retailing, 96(1), 25–39.
- Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. Management Information Systems Quarterly, 45(1), 315–341.
- Cui, R., et al. (2022). Field experiment on B2B sourcing platform comparing AI and human procurement agents.
- Lebovitz, S., et al. (2021). Performance of AI tools in hospitals: A comparative study.
```
  
### Outlook: incoming features and improvements
- Add tabular database for all created summaries (to reduce API calls and make questions on counts more reliable)
- Improve existing guidance prompts for RAG (there are still issues which need to be resolved)
- Give user the option to easily create and add guidance prompts
- Enhance user interface while keeping the copy-ability of markdown formatting and make sure history and all returned messages are accessible
- For better reproducability the temperature has to be *0*, but for real-world use, this should be adjusted
- Include the option of the user to select the LLM (for higher reproducability this is fixed)
