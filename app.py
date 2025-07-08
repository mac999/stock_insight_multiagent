import gradio as gr
from insight_agent_lite.agent import InsightAgentLite

agent = InsightAgentLite()

# Simple in-memory stores for files and API keys
uploaded_files = []
api_keys = {"stock": "", "search": ""}


def handle_chat(message, history):
    response = agent.answer(message)
    return response


def upload_pdf(files):
    uploaded_files.extend(files)
    return [f.name for f in uploaded_files]


def save_stock_key(key):
    api_keys["stock"] = key
    return "Saved"


def save_search_key(key):
    api_keys["search"] = key
    return "Saved"


with gr.Blocks() as demo:
    gr.Markdown("# Insight Agent Lite")
    chat = gr.ChatInterface(handle_chat)
    with gr.Accordion("Files & API Keys", open=False):
        gr.Markdown("### Upload PDF Reports")
        file_uploader = gr.File(label="Upload", file_types=[".pdf"],
                                file_count="multiple")
        file_uploader.upload(upload_pdf, file_uploader, gr.State())
        file_list = gr.Markdown("No files uploaded")
        file_uploader.change(lambda fs: "\n".join([f.name for f in uploaded_files]),
                             None, file_list)
        gr.Markdown("### API Keys")
        stock_key = gr.Textbox(label="Stock Data API Key", type="password")
        stock_key.submit(save_stock_key, stock_key)
        search_key = gr.Textbox(label="Web Search API Key", type="password")
        search_key.submit(save_search_key, search_key)

if __name__ == "__main__":
    demo.launch()
