
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# --------------------
# Scoring Functions
# --------------------
def trust_score(profile):
    # Account age (0–40 points)
    age_days = profile["age_days"]
    age_points = min(age_days / 365, 1) * 40

    # Follower/following ratio (0–30 points)
    ratio = profile["followers"] / max(1, profile["following"])
    ratio_points = min(ratio, 1) * 30

    # Number of posts (0–30 points)
    posts_points = min(len(profile["posts"]) / 10, 1) * 30

    total = age_points + ratio_points + posts_points
    return round(total, 2)

def label(score):
    if score < 35:
        return "Likely fake/bot"
    elif score < 65:
        return "Suspicious"
    else:
        return "Likely real"

# --------------------
# GUI Functions
# --------------------
def analyze():
    try:
        username = entry_username.get().strip()
        age_days = int(entry_age.get().strip())
        followers = int(entry_followers.get().strip())
        following = int(entry_following.get().strip())
        posts_raw = text_posts.get("1.0", tk.END).strip()
        posts = [p.strip() for p in posts_raw.split("\n") if p.strip()]

        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        profile = {
            "username": username,
            "age_days": age_days,
            "followers": followers,
            "following": following,
            "posts": posts
        }

        score = trust_score(profile)
        lbl = label(score)

        result_text.set(f"Trust Score: {score}/100\nVerdict: {lbl}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for age, followers, and following.")

# --------------------
# GUI Layout
# --------------------
root = tk.Tk()
root.title("Profile Purity Detector")

# Username
tk.Label(root, text="Username:").grid(row=0, column=0, sticky="w")
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=0, column=1)

# Account Age (days)
tk.Label(root, text="Account Age (days):").grid(row=1, column=0, sticky="w")
entry_age = tk.Entry(root, width=30)
entry_age.grid(row=1, column=1)

# Followers
tk.Label(root, text="Followers:").grid(row=2, column=0, sticky="w")
entry_followers = tk.Entry(root, width=30)
entry_followers.grid(row=2, column=1)

# Following
tk.Label(root, text="Following:").grid(row=3, column=0, sticky="w")
entry_following = tk.Entry(root, width=30)
entry_following.grid(row=3, column=1)

# Posts
tk.Label(root, text="Posts (one per line):").grid(row=4, column=0, sticky="nw")
text_posts = tk.Text(root, width=40, height=5)
text_posts.grid(row=4, column=1)

# Analyze Button
btn_analyze = tk.Button(root, text="Analyze Profile", command=analyze)
btn_analyze.grid(row=5, column=0, columnspan=2, pady=10)

# Result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), fg="blue")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
