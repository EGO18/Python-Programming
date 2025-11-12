from nicegui import ui

# Get Hash
def get_hash():
    name = input_field.value.strip()

# Layout
ui.label('Welcome').style("color: Black; font-size: 40px")
with ui.row().classes("w-120"):
    with ui.column().classes("flex-1"):
        with ui.card().classes("h-65 w-120 self-auto"):
            ui.label("Hashing").style("font-size: 30px")
            input_field = ui.input("Enter your name")
            ui.label("Hash value: ").style("font-size: 30px")            
            ui.button("GET HASH", on_click=get_hash, color="blue")

ui.run(title = "Hashing")