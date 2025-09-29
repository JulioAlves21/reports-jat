from odoo import tools
from odoo import models, fields, api

class ReportCovid19WithDates(models.AbstractModel):
    _name = 'reports.report_charge'
    _description = 'COVID-19 report with dates'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'reports.sale.report.wizard',
            'docs': self.env['reports.sale.report.wizard'].browse(docids),
            'report_type': data.get('report_type') if data else '',
        }
