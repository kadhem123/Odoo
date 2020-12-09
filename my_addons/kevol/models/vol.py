from odoo import models, fields

class KeolVol(models.Model):
    _name = 'kevol.vol'
    dateDepart = fields.Datetime('Date depart')
    dateArrive = fields.Datetime('Date arrivée')
    villeDepart = fields.Char('Ville depart')
    villeArrive = fields.Char('Ville arrivée')
    retard = fields.Char('Retard')
    avion_id = fields.Many2one(comodel_name='kevol.avion')
    pilote_id = fields.Many2one(comodel_name='kevol.pilote')
    passager_ids = fields.One2many(comodel_name='kevol.passager',
                                  inverse_name='vol_id')
    compagnie_ids = fields.One2many(comodel_name='kevol.compagnie',
                                  inverse_name='vol_id')


