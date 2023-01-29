from ajax_datatable.views import AjaxDatatableView
from .models import pondok


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
                status = "Indikator 7"

        row['status_pondok'] = status
        row['action'] = f"""<a href="#" class="btn btn-sm btn-primary"  onclick="detail('{row['pk']}');">Halaman Indikator</a>
         <a href="#" class="btn btn-sm btn-primary"  onclick="evaluasi('{row['pk']}');">Halaman Evaluasi</a>
         """
