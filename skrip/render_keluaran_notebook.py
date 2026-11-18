"""Merender sel notebook (kode + keluaran teks/gambar) menjadi PNG bergaya notebook netral.

Dipakai untuk gambar keluaran notebook di naskah buku (Bab 4-7, 10, 12).
Prasyarat: Pillow, Node.js dengan paket `playwright` (Chromium).
Langkah: (1) jalankan notebook dengan scikit-learn <= 1.8 dari akar repositori
(mis. dengan nbclient) agar keluarannya segar; (2) panggil render(path_ipynb, [indeks_sel], 'keluar.png').
Sel dengan kode lebih dari 28 baris ditampilkan tanpa kode, hanya keluarannya.
Berkas .html dan .js perantara ditulis di samping PNG; skrip Node dijalankan dari folder kerja saat ini.
"""
import json,sys,html,base64,io,subprocess,os
from PIL import Image
def render(nb_path,cells,out_png,cap='',show_src=True,maxsrc=28):
    nb=json.load(open(nb_path)); parts=[]
    for ci in cells:
        c=nb['cells'][ci]; src=''.join(c['source']); n=c.get('execution_count') or ci
        lines=src.splitlines()
        if show_src and len(lines)<=maxsrc:
            parts.append(f"<p class='lab'>Masukan [{n}]</p><pre class='in'>{html.escape(src)}</pre>")
        outs=[]
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': outs.append(('t',''.join(o['text'])))
            elif 'data' in o:
                if 'image/png' in o['data']: outs.append(('i',o['data']['image/png']))
                elif 'text/plain' in o['data']: outs.append(('t',''.join(o['data']['text/plain'])))
        if outs:
            parts.append("<p class='lab'>Keluaran</p>")
            for k,v in outs:
                if k=='t': parts.append(f"<pre class='out'>{html.escape(v.rstrip())}</pre>")
                else:
                    im=Image.open(io.BytesIO(base64.b64decode(v))); w=min(im.width,900)
                    parts.append(f"<div class='img'><img src='data:image/png;base64,{v}' style='width:{w}px'></div>")
    css="""body{margin:0;background:#fff;font-family:'DejaVu Sans Mono',monospace;color:#1f2328}
.w{padding:18px 22px;width:1200px}.lab{font:600 13px 'DejaVu Sans',sans-serif;color:#57606a;margin:0 0 6px}
pre{margin:0 0 16px;padding:12px 14px;font-size:15px;line-height:1.38;white-space:pre-wrap;overflow-wrap:anywhere;border-radius:6px;overflow:hidden}
.in{background:#f6f8fa;border:1px solid #d0d7de}.out{background:#fff;border:1px solid #d0d7de}.img{margin:0 0 16px;border:1px solid #d0d7de;border-radius:6px;padding:8px;display:inline-block}"""
    h=f"<html><head><meta charset='utf-8'><style>{css}</style></head><body><div class='w' id='c'>{''.join(parts)}</div></body></html>"
    hp=out_png.replace('.png','.html'); open(hp,'w').write(h)
    js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{deviceScaleFactor:2,viewport:{{width:1300,height:600}}}});await p.goto('file://{hp}');const el=await p.$('#c');await el.screenshot({{path:'{out_png}'}});await b.close()}})();"
    jp=out_png.replace('.png','.js'); open(jp,'w').write(js)
    subprocess.run(['node',jp],check=True,cwd=os.getcwd())
if __name__=='__main__':
    render(sys.argv[1],[int(x) for x in sys.argv[2].split(',')],sys.argv[3])
