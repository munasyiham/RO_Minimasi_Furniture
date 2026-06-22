import streamlit as st
from solver.lp_solver import solve_problem
from solver.visualization import plot_graph

st.set_page_config(
    page_title="Optimasi Produksi Furniture",
    layout="wide"
)

# ==========================
# HEADER
# ==========================
st.title("Optimasi Produksi Furniture")
st.markdown("### Linear Programming Metode Grafik (Persoalan Minimasi)")

st.info("""
Studi Kasus:
Perusahaan furniture memproduksi Meja (x) dan Kursi (y).
Memiliki tujuan untuk menentukan kombinasi produksi dengan biaya minimum
yang tetap memenuhi kebutuhan minimum sumber daya produksi.
""")

st.markdown("---")

# ==========================
# INPUT
# ==========================

col1, col2 = st.columns(2)

with col1:
    st.subheader("Fungsi Tujuan")

    with st.container(border=True):
        biaya_meja = st.number_input(
            "Biaya Produksi Meja (x)",
            value=100
        )

        biaya_kursi = st.number_input(
            "Biaya Produksi Kursi (y)",
            value=70
        )

with col2:
    st.subheader("Kendala Produksi")

    with st.container(border=True):

        tab1, tab2 = st.tabs(
            ["Kayu", "Tenaga Kerja"]
        )

        with tab1:

            k1x = st.number_input(
                "Koef. Meja (Kayu)",
                value=2
            )

            k1y = st.number_input(
                "Koef. Kursi (Kayu)",
                value=1
            )

            k1hasil = st.number_input(
                "Target Minimum Kayu",
                value=30
            )

        with tab2:

            k2x = st.number_input(
                "Koef. Meja (Tenaga Kerja)",
                value=1
            )

            k2y = st.number_input(
                "Koef. Kursi (Tenaga Kerja)",
                value=3
            )

            k2hasil = st.number_input(
                "Target Minimum Tenaga Kerja",
                value=45
            )

st.markdown("###")

# ==========================
# PROSES
# ==========================

if st.button(
    "Hitung Optimasi",
    use_container_width=True,
    type="primary"
):

    hasil = solve_problem(
        biaya_meja,
        biaya_kursi,
        k1x,
        k1y,
        k1hasil,
        k2x,
        k2y,
        k2hasil
    )

    if hasil.success:

        st.success(
            "Solusi Optimal Berhasil Ditemukan"
        )

        res_col1, res_col2 = st.columns([1, 2])

        with res_col1:

            st.subheader("Model Matematika")

            st.latex(
                f"Min\\ Z = {biaya_meja}x + {biaya_kursi}y"
            )

            st.latex(
                f"{k1x}x + {k1y}y \\geq {k1hasil}"
            )

            st.latex(
                f"{k2x}x + {k2y}y \\geq {k2hasil}"
            )

            st.latex(
                "x,y \\geq 0"
            )

            st.subheader("Hasil Optimasi")

            st.metric(
                "Jumlah Meja (x)",
                f"{hasil.x[0]:.2f}"
            )

            st.metric(
                "Jumlah Kursi (y)",
                f"{hasil.x[1]:.2f}"
            )

            st.metric(
                "Biaya Minimum",
                f"Rp {hasil.fun:,.0f}"
            )

        with res_col2:

            st.subheader("Visualisasi Grafik")

            fig = plot_graph(
                k1x,
                k1y,
                k1hasil,
                k2x,
                k2y,
                k2hasil,
                hasil.x[0],
                hasil.x[1]
            )

            st.pyplot(fig)

    else:

        st.error(
            "Tidak ditemukan solusi yang memenuhi seluruh kendala."
        )