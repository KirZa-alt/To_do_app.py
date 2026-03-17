import streamlit as st

st.set_page_config(page_title="Smart To-Do App", page_icon="✅")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "➕ Add Task", "📋 Task List", "📊 Progress"]
)

# Home
if menu == "🏠 Home":
    st.title("🚀 Smart To-Do List")
    st.write("Manage your tasks easily!")

# Add Task
elif menu == "➕ Add Task":

    st.header("Add Task")

    task_name = st.text_input("Task Name")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    if st.button("Add Task"):
        if task_name != "":
            st.session_state.tasks.append({
                "name": task_name,
                "priority": priority,
                "done": False
            })
            st.success("Task Added!")

# Task List
elif menu == "📋 Task List":

    st.header("Your Tasks")

    if len(st.session_state.tasks) == 0:
        st.info("No tasks yet")

    for i, task in enumerate(st.session_state.tasks):

        col1, col2, col3, col4 = st.columns([4,2,1,1])

        with col1:
            if task["done"]:
                st.write(f"~~{task['name']}~~")
            else:
                st.write(task["name"])

        with col2:
            st.write(task["priority"])

        with col3:
            if not task["done"]:
                if st.button("✔", key=f"done{i}"):
                    st.session_state.tasks[i]["done"] = True
                    st.balloons()

        with col4:
            if st.button("🗑", key=f"del{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

# Progress
elif menu == "📊 Progress":

    total = len(st.session_state.tasks)
    completed = len([t for t in st.session_state.tasks if t["done"]])

    if total > 0:
        progress = completed / total
        st.progress(progress)

        st.write("Completed:", completed)
        st.write("Total:", total)

    else:
        st.info("Add tasks first")