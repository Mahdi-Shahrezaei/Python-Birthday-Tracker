 # For Download exe & Source code This Particular App -> Telegram : @AI172 Contact : In @AI172

# ⚡ High-Performance Grid & Persistence Logic
class DayInfo:
    def __init__(self, number, is_done, widget):
        self.number = number
        self.is_done = is_done
        self.widget = widget

def click_handler(idx):
    btn = all_buttons[idx]
    if not btn.is_done:
        btn.is_done = True
        btn.widget.config(bg="#2ecc71") # Instant Green Feedback
        update_counter()
        save_to_disk() # Auto-syncing progress...

# Mapping 365 days into a seamless 21-column grid
for i in range(365):
    btn_widget.grid(row=i // 21, column=i % 21, padx=1, pady=1)
