"""Mengambil tangkapan layar Orange (kanvas dan widget) dari berkas .ows tanpa layar fisik.

Dipakai untuk Gambar 4.2, 5.3, 6.3, 7.2, 8.2, 9.1, 10.2, 12.2, 13.2, 14.2, dan 15.2.

Prasyarat: orange3 3.41, PyQt5, PyQtWebEngine, dan Xvfb.
Contoh (dari akar repositori):
  xvfb-run -a -s "-screen 0 2000x1000x24" python skrip/tangkap_orange.py \\
    praktikum/bab04/Orange_Bab4_Regresi.ows keluaran/b4 \\
    praktikum/bab04/data_bab4/data_sintesis_kuat_tekan.csv kuat_tekan_MPa id_spesimen

Argumen: berkas.ows  folder_keluaran  data  target  meta1,meta2  [konfigurasi JSON widget]
Untuk data CSV, skrip membuat berkas .tab sementara di /tmp/shots agar target dan
metadata terpasang seperti hasil akhir langkah Select Columns. Workflow .ows tidak
menyimpan jalur data (lihat README tiap bab).
"""
import sys,os,re,time,json
from AnyQt.QtCore import QTimer, QCoreApplication
from Orange.canvas.__main__ import OMain
R=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))+'/'
ows,out,data,target,metas=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5].split(',') if sys.argv[5] else []
os.makedirs(out,exist_ok=True)
CFG=json.loads(sys.argv[6]) if len(sys.argv)>6 else {}
def prep():
    if data.endswith('.tab'): return data
    import Orange
    from Orange.data import Table, Domain
    t=Table.from_file(data)
    d=t.domain; allv=list(d.variables)+list(d.metas)
    cv=[v for v in allv if v.name==target]
    mv=[v for v in allv if v.name in metas]
    attrs=[v for v in allv if v not in cv and v not in mv]
    nt=Table.from_table(Domain(attrs,cv[0] if cv else None,mv),t)
    for nm in CFG.get('categorical',[]):
        # kolom numerik berkode (mis. label_pembangkit 0-3) dijadikan kategorikal, setara mengubah tipe kolom pada widget File
        import numpy as np
        from Orange.data import DiscreteVariable
        v=[m for m in nt.domain.metas if m.name==nm][0]; j=list(nt.domain.metas).index(v)
        vals=sorted({str(int(x)) for x in nt.metas[:,j]}); dv=DiscreteVariable(nm,values=tuple(vals))
        meta2=[dv if m is v else m for m in nt.domain.metas]; M=nt.metas.copy().astype(object)
        M[:,j]=[vals.index(str(int(x))) for x in nt.metas[:,j]]
        nt=Table.from_numpy(Domain(nt.domain.attributes,nt.domain.class_vars,meta2),nt.X,nt.Y if nt.Y.size else None,M)
    p=f'/tmp/shots/_{os.path.basename(data)[:-4]}.tab'; nt.save(p); return p
class M(OMain):
    def setup_application(self):
        super().setup_application(); QTimer.singleShot(12000,self.go)
    def go(self):
        from AnyQt.QtWidgets import QApplication
        app=QApplication.instance()
        try:
            win=[w for w in app.topLevelWidgets() if w.__class__.__name__.endswith('MainWindow') and w.isVisible()][0]
            win.resize(1900,800); app.processEvents(); time.sleep(1); doc=win.current_document(); sch=doc.scheme()
            f=[n for n in sch.nodes if n.title=='File'][0]; fw=sch.widget_for_node(f)
            p=prep(); fw.add_path(p); fw.source=fw.LOCAL_FILE; fw.load_data()
            for _ in range(40): app.processEvents(); time.sleep(0.2)
            time.sleep(6)
            for _ in range(40): app.processEvents(); time.sleep(0.2)
            def V(w,name):
                return None if not name else w.data.domain[name] if hasattr(w,'data') and w.data is not None and name in w.data.domain else None
            for n in sch.nodes:
                w=sch.widget_for_node(n)
                try:
                    if n.title=='Distributions' and 'dist' in CFG:
                        dom=w.data.domain; allv={v.name:v for v in list(dom.variables)+list(dom.metas)}
                        w.var=allv[CFG['dist'][0]]; w._on_var_changed()
                        if 'bins' in CFG: w.number_of_bins=CFG['bins']; w._on_bin_slider_released()
                        if CFG['dist'][1]: w.cvar=allv[CFG['dist'][1]]; w._on_cvar_changed()
                    if n.title=='Scatter Plot' and 'scat' in CFG:
                        dom=w.data.domain; allv={v.name:v for v in list(dom.variables)+list(dom.metas)}
                        x,y,c=CFG['scat']; w.attr_x=allv[x]; w.attr_y=allv[y]; w.attr_changed()
                        if c: w.attr_color=allv[c]; w.attr_changed()
                    if n.title=='Box Plot' and 'box' in CFG:
                        dom=w.dataset.domain; allv={v.name:v for v in list(dom.variables)+list(dom.metas)}
                        a,g=CFG['box']; w.attribute=allv[a]; w.group_var=allv[g] if g else None
                        w._set_list_view_selections(); w._variables_changed(w.apply_attr_sorting)
                    if n.title=='Pivot Table' and 'pivot' in CFG:
                        dom=w.data.domain; allv={v.name:v for v in list(dom.variables)+list(dom.metas)}
                        r,c=CFG['pivot']; w.row_feature=allv[r]; w.col_feature=allv[c]; w._OWPivot__feature_changed()
                except Exception as e:
                    print('cfg gagal',n.title,e,flush=True)
            for _ in range(30): app.processEvents(); time.sleep(0.1)
            (doc.view().scene().clearSelection(), app.processEvents(), doc.view().grab())[-1].save(f'{out}/canvas.png')
            for i,n in enumerate(sch.nodes):
                w=sch.widget_for_node(n); w.show()
                if n.title in CFG.get('resize',{}): w.resize(*CFG['resize'][n.title]); app.processEvents()
                for _ in range(30): app.processEvents(); time.sleep(0.1)
                time.sleep(2); app.processEvents()
                w.grab().save(f'{out}/{i:02d}_{re.sub(r"\W+","_",n.title)}.png')
            print('selesai',flush=True)
        except Exception:
            import traceback; traceback.print_exc()
        finally: QCoreApplication.quit()
M().run(['canvas','--no-welcome','--no-splash',R+ows])
