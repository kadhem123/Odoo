from odoo import models, fields

class KeolVol(models.Model):
    _name = 'kevol.vol'
    name=fields.Char("numero vol")
    dateDepart = fields.Datetime('Date depart')
    dateArrive = fields.Datetime('Date arrivée')
    villeDepart = fields.Char('Ville depart')
    villeArrive = fields.Char('Ville arrivée')
    retard = fields.Char('Retard')
    avion_id = fields.Many2one(comodel_name='kevol.avion')
    pilote_id = fields.Many2one(comodel_name='kevol.pilote')
    billet_id = fields.One2many(comodel_name='kevol.billet',
                                inverse_name='vol_id')



