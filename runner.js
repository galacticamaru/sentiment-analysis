if runner:
    from IPython.display import display, Javascript

    display(
        Javascript(
            "IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1, len(IPython.notebook.cells))"
        )
    )
