from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ChargeReportWizard(models.TransientModel):
    _name = "sale.report.wizard"
    _description = "Reportes Carga JAT"
    
    
    start_date=fields.Date('Start Date',required=True)
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
        produ = self.get_qty_product(CovidRecords)
        data = {
            'productos':produ,
            'desde': self.start_date,
            'hasta': self.end_date,
            'empleado': self.user_id.name,
        }
        return  self.env.ref('report.reportcharge').report_action(self, data=data)
    
    def get_qty_product(self,data):
        ventas=self.env['sale.order.line']
        products = []
        for sale_order in data:
                for order_line in sale_order:
                    for product in order_line.order_line:
                        encontro = False
                        for item in products:
                            if item["nombre"] == product.product_id.name:
                                encontro = True
                        if encontro == False:    
                            products.append({"nombre":product.product_id.name,"cant":product.product_uom_qty})
                        else:
                            for item in products:
                                if item["nombre"] == product.product_id.name:
                                   item["cant"] = item["cant"] + product.product_uom_qty
        #Fuciona                  
        return products





