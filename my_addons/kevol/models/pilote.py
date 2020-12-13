from odoo import models, fields

class KevolPilote(models.Model):
    _name = 'kevol.pilote'
    name = fields.Char('Nom Pilote')
    qualif = fields.Char('Qualifications')
    compagnie_id = fields.Many2one(comodel_name='kevol.compagnie')

    vol_id = fields.One2many(comodel_name='kevol.vol',
                             inverse_name='pilote_id')





