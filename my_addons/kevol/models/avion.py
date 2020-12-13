from odoo import models, fields

class KevolAvion(models.Model):
    _name = 'kevol.avion'
    type = fields.Char('Type Avion')
    _rec_name = 'modele'
    modele = fields.Char('Modele Avion')
    nb = fields.Char('Nombre passagers')
    siege_ids = fields.One2many(comodel_name='kevol.siege',
                               inverse_name='avion_id')
    pilote_ids = fields.Many2many(comodel_name='kevol.pilote',
                                    relation='class_pilote_rel',
                                    column1='name',
                                    column2='prenom')
    vol_id = fields.One2many(comodel_name='kevol.vol',
                             inverse_name='avion_id')

