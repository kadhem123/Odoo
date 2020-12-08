from odoo import models, fields

class VolVol(models.Model):
    _name = 'vol.vol'
    date_depart = fields.Datetime('Date depart')
    date_arrivée = fields.Datetime('Date arrivée')
    ville_depart = fields.Char('Ville depart')
    ville_arrivee = fields.Char('Ville arrivée')
    retard = fields.Char('Retard')
