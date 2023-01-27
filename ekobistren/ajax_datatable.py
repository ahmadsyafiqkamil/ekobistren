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
        {'name': 'status', 'title': "Status Pondok", 'visible': True, 'orderable': True, },
        {'name': 'action', 'title': 'Aksi', 'searchable': False, 'orderable': False, },
    ]

    def customize_row(self, row, obj):
        row['action'] = f"""
                                        <a href="#" class="btn btn-primary" id="add" 
                                            onclick="detail('{row['pk']}'); " >
                                               Detail
                                            </a>
                                    """