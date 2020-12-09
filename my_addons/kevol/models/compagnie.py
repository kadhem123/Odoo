from odoo import models, fields

class KevolCompagnie(models.Model):
    _name = 'kevol.compagnie'
    name = fields.Char('Nom Compagnie')
    siege_social = fields.Char('Siége Social')
    pilote_id = fields.One2many(comodel_name='kevol.pilote',
                                inverse_name='compagnie_id')
    vol_id = fields.Many2one(comodel_name='kevol.vol')
    compagnie_ids = fields.One2many(comodel_name='kevol.compagnie',
                                  inverse_name='vol_id')

