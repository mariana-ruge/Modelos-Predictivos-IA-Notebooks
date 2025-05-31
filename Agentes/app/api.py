from typing import Union

from fastapi import FastAPI

from agent import graph

app = FastAPI()


@app.get("/")
def agent():
    return graph.invoke({"customer_name": "Mariana", "my_var": "Hello"})




