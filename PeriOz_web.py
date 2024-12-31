
import os
import sys
import gradio as gr
from modules import gr_components as gc
from datetime import datetime
import multiprocessing



css="""

    .my-table-container {
        font-family:inherit !important;
        max-height: 400px;
        overflow-y: auto;
        border: 0.5px solid gray !important;
        padding: 10px;
        width:100%;
        margin:auto;
    }
    .my-table-wrapper {
        display: flex;
        justify-content: center;
    }
    .table {
        width: 100%;
        font-family:inherit;
        border:0.5px solid gray;
    }
    .dataframe{
        width:100%;
    }

    table { width: 100%; }
    
    
    """
if __name__=="__main__":
    multiprocessing.set_start_method("spawn", force=True)
    with gr.Blocks(css=css) as UI:
        gc.gr_components()
    UI.launch(debug=True,share=True)


