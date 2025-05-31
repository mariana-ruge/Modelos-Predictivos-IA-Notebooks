# Traer el diccionario para los estados
from typing import TypedDict

# Traer el grafo con nodo final
from langgraph.graph import StateGraph, END

# Estado inicial de langgraph
from langgraph.constants import START

# Estados de los comportamientos de los agentes
class State(TypedDict, total=False):
    name: str
    age: int
    customer_name: str
    var: str
    my_var: str

# Definir los nodos del agente
def node_start(state: State) -> State:
    state["var"] = "Hello"
    return state

def node_1(state: State) -> State:
    customer_name = state.get("customer_name", "user")
    state["my_var"] = f"Hello {customer_name}"
    return state

def node_2(state: State) -> State:
    return state

# Definir el grafo
builder = StateGraph(State)

# Añadir nodos al grafo
builder.add_node("start", node_start)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)

# ✅ Línea que faltaba: conectar START
builder.set_entry_point("start")
# Alternativa: graph.add_edge(START, "start")

# Añadir aristas (flujo entre nodos)
builder.add_edge("start", "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", END)

# Compilar el grafo
graph = builder.compile()

