from odoo import models, fields

class KevolCompagnie(models.Model):
    _name = 'kevol.compagnie'
    name = fields.Char('Nom Compagnie')
    siege_social = fields.Char('Siége Social')
    pilote_ids = fields.One2many(comodel_name='kevol.pilote',
                                inverse_name='compagnie_id')


