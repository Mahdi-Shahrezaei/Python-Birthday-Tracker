

# 🚀 Birthday Tracker Pro (365-Day Journey)
For Download This Particular App -> Telegram : @AI172

Contact : In @AI172

![Python](https://img.shields.io/badge/python-36.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

![Birthday Tracker 365](https://github.com/Mahdi-Shahrezaei/Python-Birthday-Tracker/blob/main/BT365.png)
> **"Don't just count the days, make the days count."**  
> A minimalist, high-performance dark-mode tracker designed to visualize your journey from July 11th to the next year.


## 🛠 Key Features (The "Cool" Stuff)
*   🌓 **Pure Dark Mode Aesthetics:** Designed for eye comfort and a sleek modern look.
*   🎯 **Zero-Scroll Grid Layout:** 365 days perfectly mapped in a single view.
*   💾 **Smart Persistence:** Your progress is automatically synced to a local database (`.txt`) so you never lose a single day.
*   ⚡ **Instant Feedback:** Real-time age tracking and countdown updates with every click.
*   🌱 **Minimalist Core:** No heavy dependencies, just pure, fast Python logic.


 💎 Code Snippet: The Magic Behind the UI

python
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

# 🏗 Installation & Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/birthday-tracker.git
   ```
2. Run the app:
   ```bash
   python tracker.py
   ```

👨‍💻 Built with ❤️ by [M.SH.420](https://github.com/YOUR_USERNAME)
If you liked this project, feel free to ⭐ the repo!*
