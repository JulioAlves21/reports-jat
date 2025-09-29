from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleReportWizard(models.TransientModel):
    _name = "ventas.report.wizard"
    _description = "Reportes ventas JAT"
    
    
    start_date=fields.Date('Start Date',required=True)
    total = 0
    end_date=fields.Date('End Date',required=True)
    user_id = fields.Many2one(
                                    "res.users", 
                                    string="Vendedores", 
                                    help="Seleccionar reporte de vendedores a "
                                    )




    def print_report(self):
        ventas=self.env['sale.order']
            
        domain=[
                            ('date_order','>',self.start_date),
                            ('date_order','<',self.end_date),
                            ('user_id','in',self.user_id.ids)
                            ]
        CovidRecords=ventas.search(domain)
        #print(CovidRecords)
        pedidos = self.get_qty_product(CovidRecords)
        data = {
            'pedidos':pedidos,
            'desde': self.start_date,
            'hasta': self.end_date,
            'empleado': self.user_id.name,
            'total': self.total
        }
        print(data)
        return  self.env.ref('report.reportsale').report_action(self, data=data)
    
    def get_qty_product(self,data):
        pedidos = []
        for sale_order in data:
            pedidos.append({"pedido":sale_order.id,"cliente":sale_order.partner_id.name,"total":sale_order.amount_total})
            self.total = self.total + sale_order.amount_total
        return  pedidos            
