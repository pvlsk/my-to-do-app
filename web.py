import streamlit as st
import functions as f

def add_todo():
    #grab user's input
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)

todos = f.get_todos()

st.title("My Todo App")
st.subheader("This is mytodo app.")
st.write('This app will increase your productivity')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')