
import pytest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch
from quickbanks import QuickBankPro


@pytest.fixture
def app():
    root = tk.Tk()
    root.withdraw()  # Hide window during tests
    app = QuickBankPro(root)
    yield app
    root.update_idletasks()
    try:
        root.destroy()
    except:
        pass  # Ignore if already destroyed


def test_initial_state(app):
    assert app.items == []
    assert app.total_var.get() == "TOTAL: $0.00"
    assert app.cust_entry.get() == ""
    assert app.qty_entry.get() == "1"


def test_add_known_piece_item(app):
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "8888888888888")      # Coca Cola piece
    app.qty_entry.delete(0, tk.END)
    app.qty_entry.insert(0, "2")

    app.add_item()

    assert len(app.items) == 1
    item = app.items[0]
    assert item["name"] == "Coca Cola 500ml"
    assert item["qty"] == 2
    assert item["unit"] == 1.99
    assert item["total"] == 3.98


def test_add_carton_barcode_auto_detect(app):
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "8888888888895")      # Coca Cola CARTON
    app.qty_entry.delete(0, tk.END)
    app.qty_entry.insert(0, "1")

    app.add_item()

    item = app.items[0]
    assert "FULL CART" in item["name"]
    assert item["qty"] == 24
    assert item["total"] == 42.00


def test_manual_carton_mode(app):
    app.carton_mode.set(True)

    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "8888888888888")      # normal Coca Cola
    app.qty_entry.delete(0, tk.END)
    app.qty_entry.insert(0, "3")

    app.add_item()

    item = app.items[0]
    assert "CARTON ×" in item["name"]
    assert item["qty"] == 72
    assert item["total"] == 126.00
    assert app.carton_mode.get() is False         # auto-reset


def test_add_new_product(app):
    with patch.object(messagebox, 'askstring', side_effect=["Milo 400g", "45"]), \
         patch.object(messagebox, 'askfloat', return_value=5.99):

        app.item_entry.delete(0, tk.END)
        app.item_entry.insert(0, "5555555555555")
        app.add_item()

        assert "5555555555555" in app.products_db
        assert app.products_db["5555555555555"]["name"] == "Milo 400g"
        assert len(app.items) == 1
        assert app.items[0]["total"] == 5.99


def test_remove_last_item(app):
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "8888888888888")
    app.add_item()
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "1234567890123")
    app.add_item()

    assert len(app.items) == 2
    app.remove_last()
    assert len(app.items) == 1
    assert "Coca Cola" in app.items[0]["name"]


def test_clear_all(app):
    app.cust_entry.insert(0, "Aisha")
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "8888888888888")
    app.add_item()

    with patch('tkinter.messagebox.askyesno', return_value=True):
        app.clear_all()

    assert app.items == []
    assert app.cust_entry.get() == ""
    assert app.total_var.get() == "TOTAL: $0.00"


def test_tax_calculation(app):
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "8888888888888")
    app.qty_entry.delete(0, tk.END)
    app.qty_entry.insert(0, "10")
    app.add_item()          # 10 × 1.99 = 19.90 → +8% = 21.49

    assert "$21.49" in app.total_var.get()


def test_payment_cash(app):
    app.item_entry.delete(0, tk.END)
    app.item_entry.insert(0, "9999999999999")   # Red Bull
    app.add_item()

    with patch('tkinter.messagebox.askyesno', return_value=True), \
         patch('tkinter.messagebox.showinfo') as mock_info:

        app.payment("CASH")

        assert app.items == []
        call_text = mock_info.call_args[0][1]
        assert "Received $3.23" in call_text   # Correct tax: 2.99 + 0.24 = 3.23