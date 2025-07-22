from odoo import models, fields, api

class FastFoodOrder(models.Model):
    _name = 'fast.food.order'
    _description = 'Commande Fast Food'
    _order = 'order_date desc'  # Tri par date décroissante

    name = fields.Char(
        string='Référence', required=True, copy=False, readonly=True,
        default=lambda self: _('New')
    )
    customer_name = fields.Char(string='Nom du client', required=True)
    order_date = fields.Datetime(string='Date de la commande', default=fields.Datetime.now)
    order_line_ids = fields.One2many(
        'fast.food.order.line', 'order_id', string='Lignes de commande'
    )
    total_amount = fields.Monetary(
        string='Montant total', compute='_compute_total', store=True
    )
    currency_id = fields.Many2one(
        'res.currency', string='Devise',
        default=lambda self: self.env.company.currency_id
    )

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('fast.food.order') or ('New')
        return super().create(vals)

    @api.depends('order_line_ids.price_subtotal')
    def _compute_total(self):
        for order in self:
            order.total_amount = sum(line.price_subtotal for line in order.order_line_ids)


class FastFoodOrderLine(models.Model):
    _name = 'fast.food.order.line'
    _description = 'Ligne de commande Fast Food'

    order_id = fields.Many2one(
        'fast.food.order', string='Commande', required=True, ondelete='cascade'
    )
    product_id = fields.Many2one('product.product', string='Produit', required=True)
    quantity = fields.Integer(string='Quantité', default=1)
    price_unit = fields.Float(string='Prix unitaire')
    price_subtotal = fields.Float(
        string='Sous-total', compute='_compute_subtotal', store=True
    )

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.price_subtotal = line.quantity * line.price_unit
