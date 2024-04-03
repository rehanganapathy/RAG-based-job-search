<h1>RAG based Job Search</h1>

This project helps you scout for jobs usings GenAI.
Below is a concise overview of the RAG-based Job Search Assistant architecture. First, you'll establish a vector store containing job posts. Following this, you upload your CV and can then query any questions related to your job search. Additionally, multiple LLM evaluations are conducted before delivering a response, ensuring it remains faithful, helpful, and relevant to the query at hand.

<div>
  <h2>Components:</h2>
  <p>1. <strong>Scrape the job posts:</strong> Execute <code>src/job_scraper.py</code> to extract job postings from LinkedIn. Customize parameters such as job title and location.</p>
  <p>2. <strong>Build a vector storage:</strong> Run <code>src/store_data.py</code> to create a vector store from the CSV file containing job posts.</p>
</div>

<div>
  <h2>Usage:</h2>
  <p>1. <strong>Start querying:</strong> Execute <code>src/main.py</code> after uploading your CV to the <code>input_cv</code> directory for job search queries.</p>
  <p>Note: Set up the <code>OPENAI_API_KEY</code> environmental variable for the demo using OpenAI's GPT-3.5 turbo language model.</p>
</div>
