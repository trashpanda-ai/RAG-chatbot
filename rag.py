import os 
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
import tiktoken
from langchain_community.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings


import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from datetime import datetime
import time

import warnings
# Suppress LangChainDeprecationWarning
warnings.filterwarnings("ignore")



llm_model =  "gpt-4o-mini"  #  "gpt-3.5-turbo" "gpt-4o-mini"

summarize_articles_prompt = """If asked for a summary, please provide a detailed analysis following EXACTLY this format:
    1. Context: Specify focus of study (specific industry, task or a broader, conceptual scope)

    2. Research Question & Summary of Key Findings

    3. Theme (choose ONE, reason):
       a) Human vs. AI: Comparative advantages between humans and AI, or scenarios where one outperforms the other
       b) Human + AI Collaboration: Type of collaboration, incl. roles of human/AI, interaction patterns

    4. Method (choose ONE, reason):
         a) Conceptual/Case Study
         b) Modeling (Stylized/Operations Research/Model)
         c) Empirical Study (Lab/Field Experiment, Secondary Data)

    5. Contribution: Main theoretical, managerial or methodological impact

    6. Future Directions & Limitations: Research gaps & constraints"""

compare_articles_prompt = """If asked for selected research, filter and then analyze EXACTLY as follows:

    1. Possible Filter Criteria
      • Themes: [Additional]
      • Methods: [Additional]
      • Other: [Additional]

    2. For EACH document Article Analysis
      • Context: Industry/task/scope
      • Research & Findings
      • Theme (ONE+reason): Human vs. AI (advantages/scenarios) OR Human+AI (roles/patterns)
      • Method (ONE+reason): Conceptual/Modeling/Empirical
      • Contribution: Theory/management/method impact
      • Limitations & Gaps

    3. Cross-Article Synthesis
      • Patterns & Trends
      • Contradictions
      • Research Gaps
      • Future Directions

    4. ALWAYS end with List of academic References [Standard format]"""


import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from datetime import datetime
import time

class SimpleRAGChat:
    def __init__(self):
        # Initialize RAG components
        # Initialize RAG components
        if os.path.exists('vectorstore'):
            self.vectorstore = FAISS.load_local("vectorstore", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        else:
            # Load and process documents
            loader = DirectoryLoader("literature/", glob="*.pdf")
            documents = loader.load()

            text_splitter = CharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                separator="\n"
            )
            splits = text_splitter.split_documents(documents)

            # Create and save vectorstore
            try:
                embeddings = OpenAIEmbeddings()
                self.vectorstore = FAISS.from_documents(splits, embeddings)
                self.vectorstore.save_local("vectorstore")
            except Exception as e:
                print(f"Error creating vector store: {e}")
                exit(1)


        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        )
        
        self.summarizer = create_retriever_tool(
            self.retriever,
            "summarize_articles",
            summarize_articles_prompt
        )
        
        self.comparer = create_retriever_tool(
            self.retriever,
            "compare_articles",
            compare_articles_prompt
        )
        
        self.llm = ChatOpenAI(
            temperature=0,
            model_name=llm_model,
            max_tokens=4000
        )
        
        self.agent_executor = create_conversational_retrieval_agent(
            self.llm,
            [self.summarizer, self.comparer],
            verbose=False
        )

        # Create chat interface with improved styling
        self.output = widgets.Output(
            layout={
                'border': '1px solid #ddd',
                'border_radius': '10px',
                'height': '500px',
                'width': '800px',
                'overflow_y': 'auto',
                'padding': '20px',
                'background-color': '#f8f9fa'
            }
        )
        
        self.input = widgets.Text(
            placeholder='Type your message and press Enter...',
            layout={
                'width': '800px',
                'padding': '10px',
                'margin': '10px 0',
                'border': '1px solid #ddd',
                'border_radius': '8px'
            }
        )
        
        # Add title
        self.title = widgets.HTML(
            value='<h2 style="color: #0065bd; font-family: Arial, sans-serif; margin-bottom: 20px;">AI Research Assistant </h2>'
        )
        
        # Bind enter key to submit
        self.input.on_submit(self.on_enter)
        
        # Display components
        display(self.title)
        display(self.output)
        display(self.input)
        
    def on_enter(self, widget):
        time.sleep(0.1)
        message = widget.value.strip()
        if message:
            widget.value = ''  # Clear input immediately
            self.process_message(message)
    
    def process_message(self, message):
        timestamp = datetime.now().strftime("%H:%M")
        with self.output:
            print(f"\nYou ({timestamp}): {message}")
            
            try:
                print("\nAssistant: Thinking...")
                response = self.agent_executor({"input": message})
                
                # Clear output and show full conversation
                clear_output(wait=True)
                print(f"\nYou ({timestamp}): {message}")
                print(f"\nAssistant ({timestamp}): {response['output']}")
            except Exception as e:
                print(f"\nError: {str(e)}")

