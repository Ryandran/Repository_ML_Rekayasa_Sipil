"""Gambar konseptual Bab 16 (ilustrasi konseptual, bukan data buku)."""
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT = "gambar/bab16/"
# 1. arsitektur MLP
fig, ax = plt.subplots(figsize=(8, 3.6)); ax.axis("off")
lay = [(8, "masukan\n(8 fitur)"), (5, "lapisan\ntersembunyi 1"), (5, "lapisan\ntersembunyi 2"), (1, "keluaran\n(kuat tekan)")]
pos = []
for k, (n, lab) in enumerate(lay):
    ys = np.linspace(-(n-1)/2, (n-1)/2, n); pos.append([(k*2.2, y*0.62) for y in ys])
    ax.text(k*2.2, 3.1, lab, ha="center", va="bottom", fontsize=9)
for k in range(3):
    for p in pos[k]:
        for q in pos[k+1]: ax.plot([p[0], q[0]], [p[1], q[1]], color="#bbbbbb", lw=0.5, zorder=1)
for k, P in enumerate(pos):
    ax.scatter(*zip(*P), s=260, color=["#4c78a8", "#f58518", "#f58518", "#54a24b"][k], zorder=2, edgecolor="k", lw=0.6)
ax.text(2.2*1.5, -3.1, "pada tiap simpul: jumlah berbobot + bias, lalu fungsi aktivasi (ReLU)", ha="center", fontsize=8.5)
ax.set_xlim(-0.6, 7.2); ax.set_ylim(-3.5, 3.9)
plt.savefig(OUT+"Gambar_16_1_Arsitektur_MLP.png", dpi=200, bbox_inches="tight"); plt.close()
# 2. fungsi aktivasi
x = np.linspace(-4, 4, 400)
fs = {"ReLU": np.maximum(0, x), "tanh": np.tanh(x), "sigmoid": 1/(1+np.exp(-x))}
fig, ax = plt.subplots(1, 3, figsize=(9, 2.6), sharex=True)
for a, (n, f) in zip(ax, fs.items()):
    a.plot(x, f, lw=2); a.axhline(0, color="gray", lw=.5); a.axvline(0, color="gray", lw=.5); a.set_title(n, fontsize=10); a.set_xlabel("masukan z")
plt.tight_layout(); plt.savefig(OUT+"Gambar_16_2_Fungsi_aktivasi.png", dpi=200); plt.close()
# 3. konvolusi
img = np.zeros((7, 7)); img[1:6, 3] = 1; img[3, 1:6] = 0.4
ker = np.array([[-1, 0, 1]]*3, float)
out = np.array([[(img[i:i+3, j:j+3]*ker).sum() for j in range(5)] for i in range(5)])
fig, ax = plt.subplots(1, 3, figsize=(9, 3.1))
for a, m, t in zip(ax, (img, ker, out), ("citra masukan 7×7", "kernel 3×3", "peta fitur 5×5")):
    a.imshow(m, cmap="gray" if m is img else "RdBu"); a.set_title(t, fontsize=10); a.set_xticks([]); a.set_yticks([])
    if m is not img:
        for (i, j), v in np.ndenumerate(m): a.text(j, i, f"{v:g}", ha="center", va="center", fontsize=8)
ax[0].add_patch(plt.Rectangle((1.5, 0.5), 3, 3, fill=False, ec="red", lw=2))
ax[1].text(1, 3.1, "", fontsize=1)
plt.tight_layout(); plt.savefig(OUT+"Gambar_16_3_Konvolusi.png", dpi=200, bbox_inches="tight", pad_inches=0.15); plt.close()
