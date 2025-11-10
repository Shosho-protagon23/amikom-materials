import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import yfinance as yf  # Untuk mengambil data saham real-time
from datetime import datetime, timedelta

# Fungsi untuk mengambil data saham
def get_stock_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

# Fungsi untuk analisis data pasar
def analyze_market_data(data):
    # Hitung return harian
    data['Daily Return'] = data['Close'].pct_change()
    
    # Statistik dasar
    mean_return = data['Daily Return'].mean()
    volatility = data['Daily Return'].std()
    cumulative_return = (data['Close'][-1] / data['Close'][0]) - 1
    
    # Hasil analisis
    results = {
        'Mean Daily Return': f"{mean_return:.4f}",
        'Volatility (Std Dev)': f"{volatility:.4f}",
        'Cumulative Return': f"{cumulative_return:.4f}"
    }
    
    return results, data

# Fungsi untuk membuat diagram
def create_plots(data, results):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    # Plot 1: Harga Penutupan
    axes[0, 0].plot(data.index, data['Close'])
    axes[0, 0].set_title('Harga Penutupan Saham')
    axes[0, 0].set_xlabel('Tanggal')
    axes[0, 0].set_ylabel('Harga')
    
    # Plot 2: Return Harian
    axes[0, 1].plot(data.index, data['Daily Return'])
    axes[0, 1].set_title('Return Harian')
    axes[0, 1].set_xlabel('Tanggal')
    axes[0, 1].set_ylabel('Return')
    
    # Plot 3: Histogram Return
    axes[1, 0].hist(data['Daily Return'].dropna(), bins=50)
    axes[1, 0].set_title('Distribusi Return Harian')
    axes[1, 0].set_xlabel('Return')
    axes[1, 0].set_ylabel('Frekuensi')
    
    # Plot 4: Volume Perdagangan
    axes[1, 1].bar(data.index, data['Volume'])
    axes[1, 1].set_title('Volume Perdagangan')
    axes[1, 1].set_xlabel('Tanggal')
    axes[1, 1].set_ylabel('Volume')
    
    plt.tight_layout()
    return fig

# Fungsi untuk menjalankan analisis dan menampilkan hasil di jendela baru
def run_analysis():
    ticker = ticker_entry.get()
    if not ticker:
        return
    
    try:
        data = get_stock_data(ticker)
        results, data = analyze_market_data(data)
        
        # Buat jendela baru untuk hasil
        result_window = tk.Toplevel(root)
        result_window.title(f"Analisis Pasar untuk {ticker.upper()}")
        
        # Frame untuk teks hasil
        text_frame = ttk.Frame(result_window)
        text_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        result_text = tk.Text(text_frame, height=10, width=50)
        result_text.pack()
        result_text.insert(tk.END, "Hasil Analisis:\n")
        for key, value in results.items():
            result_text.insert(tk.END, f"{key}: {value}\n")
        result_text.config(state=tk.DISABLED)
        
        # Frame untuk diagram
        plot_frame = ttk.Frame(result_window)
        plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        fig = create_plots(data, results)
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    except Exception as e:
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        ttk.Label(error_window, text=f"Error: {str(e)}").pack(padx=10, pady=10)

# GUI Utama
root = tk.Tk()
root.title("Analisis Data Pasar Perusahaan")

# Input untuk ticker saham
ttk.Label(root, text="Masukkan Ticker Saham (e.g., AAPL):").pack(pady=5)
ticker_entry = ttk.Entry(root)
ticker_entry.pack(pady=5)

# Tombol untuk menjalankan analisis
run_button = ttk.Button(root, text="Jalankan Analisis", command=run_analysis)
run_button.pack(pady=10)

root.mainloop()
