__author__ = "Osigwe Uchechukwu Davidcaleb"
__version__ = "5.0"
__status__ = "Production Ready"


import tkinter as tk
from tkinter.simpledialog import askstring, askfloat
from tkinter import messagebox
import json
from datetime import datetime
import os

class QuickBankPro:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickBank PRO - SHOP READY v5.0") #tried it for 5 times to get it working good like it is now
        self.root.geometry("1100x720")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#0a0a0a")

        # Hotkeys
        self.root.bind("<F4>", lambda e: self.payment("CASH"))
        self.root.bind("<F8>", lambda e: self.payment("CARD"))
        self.root.bind("<Escape>", lambda e: self.clear_all())

        self.items = []
        self.products_db = self.load_products_db()
        self.tax_rate = 0.08
        self.carton_size = 24

        self.setup_ui()
        self.update_receipt()
        self.update_totals()

    def load_products_db(self):
        default_db = {
            "8888888888888": {"name": "Coca Cola 500ml", "price": 1.99, "carton_price": 42.00},
            "1234567890123": {"name": "Lays Chips", "price": 3.49, "carton_price": 75.00},
            "9999999999999": {"name": "Red Bull 250ml", "price": 2.99, "carton_price": 65.00},

            # === CARTON BARCODES (scan this = auto full carton price) ===
            "8888888888895": {"name": "Coca Cola 500ml", "price": 42.00, "carton_price": None, "stock_type": "carton", "carton_of": "8888888888888"},
            "1234567890130": {"name": "Lays Chips Classic", "price": 75.00, "carton_price": None, "stock_type": "carton", "carton_of": "1234567890123"},
            "9999999999905": {"name": "Red Bull 250ml", "price": 65.00, "carton_price": None, "stock_type": "carton", "carton_of": "9999999999999"},
        }

        if os.path.exists("products.json"):
            try:
                with open("products.json", "r", encoding="utf-8") as f:
                    user_db = json.load(f)
                    default_db.update(user_db)
            except Exception as e:
                print("Error loading products.json:", e)
        else:
            with open("products.json", "w", encoding="utf-8") as f:
                json.dump(default_db, f, indent=2, ensure_ascii=False)
        return default_db

    def save_products_db(self):
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(self.products_db, f, indent=2, ensure_ascii=False)

    def setup_ui(self):

        # MAIN CANVAS + SCROLLBAR
        canvas = tk.Canvas(self.root, bg="#0a0a0a", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview, width=20)
        scrollable = tk.Frame(canvas, bg="#0a0a0a")

        scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # HEADER
        header = tk.Frame(scrollable, bg="#00ff00", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="QUICKBANK PRO", font=("Helvetica", 36, "bold"), fg="black", bg="#00ff00").pack(side="left", padx=30)
        tk.Label(header, text="F4 = CASH • F8 = CARD • ESC = CLEAR", font=("Arial", 16, "bold"), fg="black", bg="#00ff00").pack(side="right", padx=30)

        # CUSTOMER
        cust_frame = tk.Frame(scrollable, bg="#0a0a0a")
        cust_frame.pack(pady=12, fill="x", padx=30)
        tk.Label(cust_frame, text="Customer:", fg="#ffd700", bg="#0a0a0a", font=("Arial", 16)).pack(side="left")
        self.cust_entry = tk.Entry(cust_frame, width=40, font=("Arial", 16), bg="#222", fg="white", insertbackground="white")
        self.cust_entry.pack(side="left", padx=20)

        # INPUT ROW
        input_frame = tk.Frame(scrollable, bg="#0a0a0a")
        input_frame.pack(pady=20, fill="x", padx=30)

        tk.Label(input_frame, text="QTY:", fg="#00ff00", font=("Arial", 22, "bold")).grid(row=0, column=0, padx=10)
        self.qty_entry = tk.Entry(input_frame, width=6, font=("Arial", 22), bg="#ffff99", justify="center")
        self.qty_entry.insert(0, "1")
        self.qty_entry.grid(row=0, column=1, padx=10)
        self.qty_entry.focus_set()

        # CARTON BUTTON
        self.carton_mode = tk.BooleanVar()
        self.carton_btn = tk.Checkbutton(input_frame, text="PIECES", variable=self.carton_mode,
                                         font=("Helvetica", 16, "bold"), fg="white", bg="#3498db",
                                         selectcolor="#e74c3c", relief="raised", bd=8,
                                         command=lambda: self.carton_btn.config(
                                             text="CARTON" if self.carton_mode.get() else "PIECES",
                                             bg="#e74c3c" if self.carton_mode.get() else "#3498db"))
        self.carton_btn.grid(row=0, column=2, padx=40)

        tk.Label(input_frame, text="BARCODE:", fg="black", font=("Arial", 18, "bold")).grid(row=0, column=3, padx=30)
        self.item_entry = tk.Entry(input_frame, width=38, font=("Arial", 18), bg="#222", fg="white", insertbackground="white")
        self.item_entry.grid(row=0, column=4, padx=10)
        tk.Button(input_frame, text="ADD", bg="#27ae60", fg="white", font=("bold", 16), width=8,
                  command=self.add_item).grid(row=0, column=5, padx=30)

        self.qty_entry.bind("<Return>", lambda e: self.item_entry.focus_set())
        self.item_entry.bind("<Return>", lambda e: self.add_item())

        # RECEIPT - FULLY FIXED
        receipt_frame = tk.Frame(scrollable)
        receipt_frame.pack(pady=15, padx=40, fill="both", expand=True)
        self.receipt_text = tk.Text(receipt_frame, font=("Courier New", 13, "bold"), bg="white", fg="black", height=18)
        receipt_scroll = tk.Scrollbar(receipt_frame, command=self.receipt_text.yview)
        self.receipt_text.config(yscrollcommand=receipt_scroll.set)
        self.receipt_text.pack(side="left", fill="both", expand=True)
        receipt_scroll.pack(side="right", fill="y")

        # TOTAL DISPLAY - FIXED
        total_frame = tk.Frame(scrollable, bg="#0a0a0a")
        total_frame.pack(pady=25)
        self.total_var = tk.StringVar(value="TOTAL: $0.00")
        tk.Label(total_frame, textvariable=self.total_var,
                 font=("Arial", 44, "bold"), fg="#ff0066", bg="black",
                 relief="raised", bd=12, padx=50, pady=15).pack()

        # BIG BUTTONS
        btn_frame = tk.Frame(scrollable, bg="#0a0a0a")
        btn_frame.pack(pady=40)
        style = {"font": ("Helvetica", 28, "bold"), "width": 12, "height": 2, "bd": 12, "relief": "raised"}

        tk.Button(btn_frame, text="CASH\nF4", bg="#27ae60", fg="white", command=lambda: self.payment("CASH"), **style).grid(row=0, column=0, padx=80)
        tk.Button(btn_frame, text="CARD\nF8", bg="#2980b9", fg="white", command=lambda: self.payment("CARD"), **style).grid(row=0, column=1, padx=80)
        tk.Button(btn_frame, text="REMOVE\nLAST", bg="#e67e22", fg="white", command=self.remove_last, **style).grid(row=1, column=0, padx=80, pady=30)
        tk.Button(btn_frame, text="CLEAR\nALL", bg="#c0392b", fg="white", command=self.clear_all, **style).grid(row=1, column=1, padx=80, pady=30)

        # Mouse wheel
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    def add_item(self):
        code = self.item_entry.get().strip()
        if not code:
            return

        try:
            qty = int(self.qty_entry.get() or "1")
            if qty < 1: qty = 1
        except:
            qty = 1

        if code not in self.products_db:
            name = askstring("New Item", "Product name?")
            if not name: return
            price = askfloat("Price", "Price per piece?", minvalue=0.01)
            if not price: return
            carton = askstring("Carton", f"Carton price for {self.carton_size} pcs? (optional)")
            carton_price = float(carton) if carton and carton.strip() else None
            self.products_db[code] = {
                "name": name,
                "price": price,
                "carton_price": carton_price,
                "stock_type": "piece"
            }
            self.save_products_db()

        prod = self.products_db[code]
        name = prod["name"]

        # === SMART CARTON DETECTION ===
        if prod.get("stock_type") == "carton":
            # This barcode is for full carton only
            unit_price = prod["price"]  # actually carton price
            total_price = unit_price * qty
            display_name = f"{name} (FULL CARTON × {qty})"
            display_qty = qty * self.carton_size  # show pieces
            display_unit = round(unit_price / self.carton_size, 3)
        elif self.carton_mode.get() and prod.get("carton_price") is not None:
            # Manual carton mode activated
            carton_price = prod["carton_price"]
            unit_price = round(carton_price / self.carton_size, 3)
            total_price = carton_price * qty
            display_name = f"{name} (CARTON × {qty})"
            display_qty = qty * self.carton_size
            display_unit = unit_price
        else:
            # Normal piece mode
            unit_price = prod["price"]
            total_price = unit_price * qty
            display_name = name
            display_qty = qty
            display_unit = unit_price

        self.items.append({
            "name": display_name[:27],
            "qty": display_qty,
            "unit": display_unit,
            "total": round(total_price, 2)
        })

        # Reset
        self.item_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.qty_entry.insert(0, "1")
        self.carton_mode.set(False)
        self.carton_btn.config(text="PIECES", bg="#3498db")
        self.qty_entry.focus_set()
        self.update_receipt()
        self.update_totals()

    def remove_last(self):
        if self.items:
            self.items.pop()
            self.update_receipt()
            self.update_totals()

    def clear_all(self):
        if not self.items or messagebox.askyesno("Clear All", "Start new customer?"):
            self.items.clear()
            self.cust_entry.delete(0, tk.END)
            self.update_receipt()
            self.update_totals()
            self.qty_entry.focus_set()

    def update_receipt(self):
        self.receipt_text.delete(1.0, tk.END)
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        customer = self.cust_entry.get().strip() or "Walk-in Customer"
        header = f"{'='*50}\n{'QUICKBANK PRO'.center(50)}\n{'Your Shop Name • 080-XXX-XXXX'.center(50)}\n{now}\nCustomer: {customer}\n{'='*50}\n\n{'ITEM':<28} {'QTY':>6} {'PRICE':>8} {'TOTAL':>10}\n{'-'*50}\n"
        self.receipt_text.insert(tk.END, header)
        for item in self.items:
            self.receipt_text.insert(tk.END, f"{item['name'][:27]:<28} {item['qty']:>6} {item['unit']:>8.2f} {item['total']:>10.2f}\n")
        subtotal = sum(item['total'] for item in self.items)
        tax = round(subtotal * self.tax_rate, 2)
        total = subtotal + tax
        footer = f"\n{'-'*50}\nSUBTOTAL{'':>36}${subtotal:>9.2f}\nTAX 8%{'':>37}${tax:>9.2f}\n{'='*50}\nTOTAL{'':>41}${total:>9.2f}\n{'='*50}\n{'THANK YOU!'.center(50)}\n"
        self.receipt_text.insert(tk.END, footer)

    def update_totals(self):
        subtotal = sum(item['total'] for item in self.items)
        tax = round(subtotal * self.tax_rate, 2)
        total = subtotal + tax
        self.total_var.set(f"TOTAL: ${total:.2f}")

    def payment(self, method):
        if not self.items:
            messagebox.showwarning("Empty Cart", "Please add items first!")
            return
        subtotal = sum(item['total'] for item in self.items)
        tax = round(subtotal * self.tax_rate, 2)
        total = subtotal + tax
        if messagebox.askyesno("Payment", f"TOTAL = ${total:.2f}\n\nPay with {method.upper()}?"):
            filename = f"RECEIPT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(self.receipt_text.get(1.0, tk.END))
            messagebox.showinfo("PAID!", f"Received ${total:.2f} via {method.upper()}\nSaved as {filename}")
            self.clear_all()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuickBankPro(root)
    root.mainloop()