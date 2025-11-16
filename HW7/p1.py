from nicegui import ui

# Get Hash
def hash(text: str) -> int:
    h = 0x9E3779B1
    for i in text:
        h =  h ^ ord(i)
        h = (h * 0x517CC1C7) & 0xFFFFFFFF
    
    h = h ^ len(text)
    return h

def get_hash():
    message = input_field.value.strip()
    result = hash(message)
    hash_label.set_text(f"Hash value: {result}")

# Layout
ui.label('Welcome').style("color: Purple; font-size: 40px")
with ui.row().classes("w-120"):
    with ui.column().classes("flex-1"):
        with ui.card().classes("h-65 w-120 self-auto"):
            ui.label("Hashing").style("color: Red; font-size: 30px")
            input_field = ui.input("Enter the word:")
            hash_label = ui.label("Hash value: ").style("font-size: 30px")            
            ui.button("GET HASH", on_click=get_hash, color="blue")

ui.switch("Dark Mode",on_change = lambda e: ui.dark_mode().enable() if e.value else ui.dark_mode().disable())
ui.run(title = "Hashing")