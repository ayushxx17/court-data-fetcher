import streamlit as st
import pandas as pd
import os
import sqlite3
from datetime import datetime

# Set up paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MENU_FILE = os.path.join(BASE_DIR, "..", "data", "menu.csv")
DB_PATH = os.path.join(BASE_DIR, "..", "db", "restaurant.db")

# Load menu
menu_df = pd.read_csv(MENU_FILE)

# Streamlit UI
st.title("🍽️ Restaurant Billing System")

order_type = st.radio("Select Order Type:", ["Dine-In", "Takeaway"])

selected_items = []
st.subheader("Menu")
for index, row in menu_df.iterrows():
    qty = st.number_input(f"{row['Item']} ({row['Price']} ₹)", min_value=0, key=index)
    if qty > 0:
        selected_items.append({
            "item": row['Item'],
            "price": row['Price'],
            "qty": qty
        })

# Bill Calculation
subtotal = sum(item["price"] * item["qty"] for item in selected_items)
gst_total = subtotal * 0.05
discount = 0.1 * subtotal if st.checkbox("Apply 10% Discount") else 0
grand_total = subtotal + gst_total - discount

st.markdown("---")
st.subheader("🧾 Bill Summary")
st.write(f"Subtotal: ₹{subtotal:.2f}")
st.write(f"GST Total (5%): ₹{gst_total:.2f}")
st.write(f"Discount: ₹{discount:.2f}")
st.write(f"**Grand Total: ₹{grand_total:.2f}**")

# Payment method
payment_method = st.selectbox("Payment Method", ["Cash", "UPI", "Card"])

# Confirm Order
if st.button("✅ Confirm Order"):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert into orders table
        cur.execute("""
            INSERT INTO orders (order_type, total_amount, gst_amount, discount, payment_method, order_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (order_type, grand_total, gst_total, discount, payment_method, now))
        order_id = cur.lastrowid

        # Insert into order_items table
        for item in selected_items:
            cur.execute("""
                INSERT INTO order_items (order_id, item_name, quantity, price)
                VALUES (?, ?, ?, ?)
            """, (order_id, item["item"], item["qty"], item["price"]))

        conn.commit()
        st.success(f"Order #{order_id} saved successfully!")

