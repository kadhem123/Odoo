from odoo import models, fields

class KevolAvion(models.Model):
    _name = 'kevol.avion'
    type = fields.Char('Type Avion')
    _rec_name = 'modele'
    modele = fields.Char('Modele Avion')
    nb = fields.Char('Nombre passagers')
    siege_ids = fields.One2many(comodel_name='kevol.siege',
                                      inverse_name='avion_id')
    compagnie_id = fields.Many2one(comodel_name='kevol.compagnie')

