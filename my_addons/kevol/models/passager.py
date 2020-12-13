from odoo import models, fields

class KevolPassager(models.Model):
    _name = 'kevol.passager'
    name = fields.Char('Nom passager')
    _rec_name = 'name'
    dateNaissance = fields.Date('Date naissance')
    telephone = fields.Char('téléphone')
    statut = fields.Char('statut')
    billet_ids = fields.One2many(comodel_name='kevol.billet',
                                inverse_name='passager_id')



