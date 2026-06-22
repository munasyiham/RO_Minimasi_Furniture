from scipy.optimize import linprog


def solve_problem(
    biaya_meja,
    biaya_kursi,
    kayu_meja,
    kayu_kursi,
    target_kayu,
    tenaga_meja,
    tenaga_kursi,
    target_tenaga
):

    # Fungsi tujuan (Minimasi)
    c = [biaya_meja, biaya_kursi]

    # Karena scipy hanya menerima <=
    # maka kendala >= diubah menjadi negatif

    A = [
        [-kayu_meja, -kayu_kursi],
        [-tenaga_meja, -tenaga_kursi]
    ]

    b = [
        -target_kayu,
        -target_tenaga
    ]

    result = linprog(
        c=c,
        A_ub=A,
        b_ub=b,
        bounds=[(0, None), (0, None)],
        method="highs"
    )

    return result