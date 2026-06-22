# Optimasi Produksi Furniture

Aplikasi **Linear Programming Metode Grafik (Persoalan Minimasi)** berbasis Streamlit untuk menentukan kombinasi produksi Meja dan Kursi dengan biaya minimum.

## Studi Kasus

Perusahaan furniture memproduksi dua jenis produk:
- **Meja (x)**
- **Kursi (y)**

Tujuan: Menentukan kombinasi produksi yang memenuhi kebutuhan minimum sumber daya (Kayu & Tenaga Kerja) dengan **biaya produksi paling rendah**.

## Cara Menjalankan

1. Install dependencies:
   ```
   pip install streamlit numpy scipy matplotlib
   ```

2. Jalankan aplikasi:
   ```
   streamlit run app.py
   ```

3. Buka browser di `http://localhost:8501`

## Struktur Proyek

```
minimasi-ro/
├── .streamlit/
│   └── config.toml          # Konfigurasi tema Streamlit
├── solver/
│   ├── __init__.py           # Package initializer
│   ├── lp_solver.py          # Solver Linear Programming (scipy)
│   └── visualization.py      # Visualisasi grafik (matplotlib)
├── app.py                    # Main aplikasi Streamlit
├── .gitignore
└── README.md
```

## Alur Aplikasi

1. **Input Pengguna** — Masukkan biaya produksi per unit dan koefisien kendala (Kayu & Tenaga Kerja)
2. **Proses Optimasi** — `solver/lp_solver.py` menggunakan `scipy.optimize.linprog` (method `highs`) untuk menyelesaikan model minimasi
3. **Output** — Menampilkan:
   - Model matematika (fungsi tujuan dan kendala dalam format LaTeX)
   - Jumlah Meja (x) dan Kursi (y) optimal
   - Biaya minimum
   - Grafik daerah feasible dengan titik optimal

## Model Matematika

**Fungsi Tujuan (Minimasi):**

```
Min Z = C₁x + C₂y
```

**Kendala:**
```
A₁₁x + A₁₂y ≥ B₁    (Kayu)
A₂₁x + A₂₂y ≥ B₂    (Tenaga Kerja)
x, y ≥ 0             (Non-negativity)
```

## Teknologi

| Library | Fungsi |
|---------|--------|
| **Streamlit** | UI/UX aplikasi web |
| **SciPy** | Solver Linear Programming (`linprog` method `highs`) |
| **Matplotlib** | Visualisasi grafik daerah feasible |
| **NumPy** | Operasi numerik untuk plotting |
