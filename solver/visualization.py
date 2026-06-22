import numpy as np
import matplotlib.pyplot as plt


def plot_graph(
    k1x, k1y, k1hasil,
    k2x, k2y, k2hasil,
    x_opt, y_opt
):

    # Rentang x untuk menggambar grafik
    x = np.linspace(0, 40, 500)

    # Garis kendala
    y1 = (k1hasil - k1x * x) / k1y
    y2 = (k2hasil - k2x * x) / k2y

    # Hilangkan nilai negatif agar grafik lebih rapi
    y1 = np.maximum(y1, 0)
    y2 = np.maximum(y2, 0)

    fig, ax = plt.subplots(figsize=(9, 6))

    # =========================
    # Garis Kendala
    # =========================
    ax.plot(
        x,
        y1,
        linewidth=2,
        label=f"{k1x}x + {k1y}y = {k1hasil}"
    )

    ax.plot(
        x,
        y2,
        linewidth=2,
        label=f"{k2x}x + {k2y}y = {k2hasil}"
    )

    # =========================
    # Daerah Feasible
    # Untuk kasus minimasi:
    # ax + by >= c
    # daerah berada di atas garis
    # =========================
    y_feasible = np.maximum(y1, y2)

    ax.fill_between(
        x,
        y_feasible,
        40,
        color="lightgreen",
        alpha=0.4,
        label="Daerah Feasible"
    )

    # =========================
    # Titik Optimal
    # =========================
    ax.scatter(
        x_opt,
        y_opt,
        color="red",
        s=180,
        zorder=5,
        label="Titik Optimal"
    )

    ax.annotate(
        f"({x_opt:.2f}, {y_opt:.2f})",
        (x_opt, y_opt),
        textcoords="offset points",
        xytext=(10, 10),
        fontsize=10,
        color="red"
    )

    # =========================
    # Tampilan Grafik
    # =========================
    ax.set_title(
        "Metode Grafik - Persoalan Minimasi",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Jumlah Meja (x)")
    ax.set_ylabel("Jumlah Kursi (y)")

    ax.set_xlim(0, 40)
    ax.set_ylim(0, 40)

    ax.grid(True, linestyle="--", alpha=0.6)

    ax.legend()

    return fig