import gradio as gr
from gradio_pdf import PDF
from llama_index.core import (
    StorageContext,
    load_index_from_storage,
)

PERSIST_DIR = "./storage"


def user_query(query, cv):

    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine(similarity_top_k=2)
    response = query_engine.query(
        f"""
            You are a career adviser. Answer a question of job seekers with given information.\n
            If their CV information is given, use that information as well to answer the question.\n
            Make sure to answer step by step and also show the reference information such as job ID at the end. \n
            If you are not sure about the answer, return NA.\n
            CV: {cv}\n
            Question: {query}"""
    )
    return response


def main(query: str, cv: str):
    response = user_query(cv, query)
    return response.response


if __name__ == "__main__":
    demo = gr.Interface(main, inputs=[gr.Textbox(label="Query"), PDF(label="CV")], outputs=gr.Textbox())
    demo.launch()
