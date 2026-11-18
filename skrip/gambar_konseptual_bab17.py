"""Gambar konseptual Bab 17 (ilustrasi konseptual, bukan data buku)."""
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
OUT = "gambar/bab17/"
rng = np.random.default_rng(3)
# 1. tiga tugas visi
base = 130 + 8 * rng.standard_normal((48, 64)); base[22:26, 8:56] -= 55; base[10:20, 40:52] -= 40
fig, ax = plt.subplots(1, 3, figsize=(10, 3.3))
for a in ax: a.imshow(base, cmap="gray", vmin=0, vmax=255); a.set_xticks([]); a.set_yticks([])
ax[0].set_title("Klasifikasi: citra ini retak?", fontsize=10); ax[0].text(2, 6, "retak: ya", color="yellow", fontsize=10, weight="bold")
ax[1].set_title("Deteksi: di mana, dan apa?", fontsize=10)
ax[1].add_patch(Rectangle((6, 19), 51, 10, fill=False, ec="lime", lw=2)); ax[1].text(7, 17, "retak 0,91", color="lime", fontsize=8)
ax[1].add_patch(Rectangle((38, 8), 15, 14, fill=False, ec="cyan", lw=2)); ax[1].text(38, 6, "lubang 0,84", color="cyan", fontsize=8)
m = np.zeros((48, 64, 4)); m[22:26, 8:56] = (1, 0, 0, .6); m[10:20, 40:52] = (0, .6, 1, .6)
ax[2].imshow(m); ax[2].set_title("Segmentasi: piksel mana?", fontsize=10)
plt.tight_layout(); plt.savefig(OUT + "Gambar_17_1_Tiga_tugas.png", dpi=200, bbox_inches="tight", pad_inches=.15); plt.close()
# 2. strategi transfer learning
fig, ax = plt.subplots(figsize=(10, 3.9)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4.2)
def blok(x, y, w, h, t, c): ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03", fc=c, ec="k", lw=.8)); ax.text(x + w/2, y + h/2, t, ha="center", va="center", fontsize=8.5)
bar = [("Lapisan awal\n(tepi, tekstur)", "#cfe2f3"), ("Lapisan tengah\n(pola)", "#cfe2f3"), ("Lapisan akhir\n(spesifik tugas)", "#fce5cd")]
for r, (jud, st) in enumerate([("A. Fitur beku + pengklasifikasi ringan", ("beku", "beku", "diganti dan dilatih")), ("B. Setel halus (fine-tuning)", ("dilatih (laju kecil)", "dilatih (laju kecil)", "diganti dan dilatih")), ("C. Dari nol", ("dilatih", "dilatih", "dilatih"))]):
    y = 2.9 - r * 1.35; ax.text(0.0, y + 0.95, jud, fontsize=9.5, weight="bold")
    for k, ((t, c), s) in enumerate(zip(bar, st)): blok(0.2 + k * 3.2, y, 2.9, 0.75, f"{t}\n[{s}]", c if r < 2 else "#eeeeee")
plt.savefig(OUT + "Gambar_17_2_Strategi_transfer_learning.png", dpi=200, bbox_inches="tight", pad_inches=.15); plt.close()
# 3. IoU dan NMS
fig, ax = plt.subplots(1, 3, figsize=(10, 3.4))
a = ax[0]; a.set_xlim(0, 10); a.set_ylim(0, 10); a.set_aspect("equal"); a.set_xticks([]); a.set_yticks([])
a.add_patch(Rectangle((1, 2), 5, 5, fill=False, ec="lime", lw=2)); a.add_patch(Rectangle((3, 3.5), 5, 5, fill=False, ec="red", lw=2)); a.add_patch(Rectangle((3, 3.5), 3, 3.5, fc="orange", alpha=.5, ec="none"))
a.set_title("IoU = irisan ÷ gabungan\n(hijau: sasaran, merah: prediksi)", fontsize=9); a.text(3.1, 4.6, "irisan", fontsize=8)
a = ax[1]; a.set_xlim(0, 10); a.set_ylim(0, 10); a.set_aspect("equal"); a.set_xticks([]); a.set_yticks([])
for (x, y, s), c in zip([(2, 2, .92), (2.6, 2.4, .85), (3.2, 2, .6), (6.5, 6, .7)], ["red"]*3 + ["blue"]): a.add_patch(Rectangle((x, y), 4, 4, fill=False, ec=c, lw=1.6)); a.text(x + .1, y + 4.15, f"{s:.2f}", fontsize=8, color=c)
a.set_title("Sebelum NMS: 4 kotak, 2 objek", fontsize=9)
a = ax[2]; a.set_xlim(0, 10); a.set_ylim(0, 10); a.set_aspect("equal"); a.set_xticks([]); a.set_yticks([])
for (x, y, s), c in zip([(2, 2, .92), (6.5, 6, .7)], ["red", "blue"]): a.add_patch(Rectangle((x, y), 4, 4, fill=False, ec=c, lw=1.8)); a.text(x + .1, y + 4.15, f"{s:.2f}", fontsize=8, color=c)
a.set_title("Sesudah NMS: kotak berskor tertinggi\ntiap kelompok dipertahankan", fontsize=9)
plt.tight_layout(); plt.savefig(OUT + "Gambar_17_3_IoU_dan_NMS.png", dpi=200, bbox_inches="tight", pad_inches=.15); plt.close()
