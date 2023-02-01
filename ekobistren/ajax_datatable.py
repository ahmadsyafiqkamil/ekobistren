from ajax_datatable.views import AjaxDatatableView
from .models import pondok, evaluasi_pondok
import json


class EvaluasiAjaxView(AjaxDatatableView):
    model = evaluasi_pondok
    code = 'evaluasi_pondok'
    title = 'Daftar Evaluasi'
    initial_order = [["nama_pondok", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'nama_pondok', 'title': "Nama Pondok", 'visible': True, },
        {'name': 'status', 'title': "Status Evaluasi", 'visible': True, },
        {'name': 'aksi', 'title': "Detil Evaluasi", 'visible': True, },
    ]

    def customize_row(self, row, obj):
        data = evaluasi_pondok.objects.get(id=row["pk"]).hasil_evaluasi
        # html = ""
        # for item in data:
        #
        #     html += f"<p>Status Pondok: {item['status_pondok']}</p>"
        #     html += f"<p>ID Ciri: {item['id_ciri']}</p>"
        #     html += f"<p>Uraian: {item['uraian']}</p>"
        #     html += "<hr>"
        #
        # html += """<a href="#" class="btn btn-sm btn-primary"  onclick="detail('{row['pk']}');">Halaman Indikator</a>"""
        status_evaluasi = evaluasi_pondok.objects.get(pk=row['pk']).status_evaluasi
        match status_evaluasi:

            case 0:
                status = "Belum di evaluasi"
                html = f"""<button type="button" class="btn btn-sm btn-primary"  onclick="detail('{row['pk']}');">Detail Evaluasi</button>"""
            case 1:
                status = "Sudah di evaluasi"
                html = f"""<button type="button" class="btn btn-sm btn-primary" disabled  onclick="detail('{row['pk']}');">Detail Evaluasi</button>"""

        row["status"] = status
        row["aksi"] = html




class PondokAjaxView(AjaxDatatableView):
    model = pondok
    code = 'pondok'
    title = 'Daftar Pondok'
    initial_order = [["nama_pondok", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'nama_pondok', 'title': "Nama Pondok", 'visible': True, },
        {'name': 'kepala_pondok', 'title': "Nama Pengasuh Pondok", 'visible': True, },
        {'name': 'alamat', 'visible': True, 'title': 'Alamat Pondok', },
        {'name': 'status_pondok', 'title': "Status Pondok", 'visible': True, 'orderable': True, },
        {'name': 'action', 'title': 'Aksi', 'searchable': False, 'orderable': False, },
    ]

    def customize_row(self, row, obj):
        # print()
        status_pondok = pondok.objects.get(pk=row['pk']).status
        match status_pondok:

            case 0:
                status = "Belum pernah melakukan evaluasi"
            case 1:
                status = "Indikator 1"
            case 2:
                status = "Indikator 2"
            case 3:
                status = "Indikator 3"
            case 4:
                status = "Indikator 4"
            case 5:
                status = "Indikator 5"
            case 6:
                status = "Indikator 6"
            case 7:
                status = "Sudah selesai melakukan evaluasi"

        row['status_pondok'] = status

        if status_pondok != 7 or status_pondok != 0:
            row['action'] = f"""<a href="#" class="btn btn-sm btn-primary"  onclick="detail('{row['pk']}');">Halaman Indikator</a>
         <a href="#" class="btn btn-sm btn-primary"  onclick="evaluasi('{row['pk']}');">Halaman Evaluasi</a>
         """
        else:
            row['action'] = f"""<a href="#" class="btn btn-sm btn-primary"  onclick="detail('{row['pk']}');">Halaman Indikator</a>
                     
                     """
