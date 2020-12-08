from odoo import models, fields

class KeolVol(models.Model):
    _name = 'kevol.vol'
    date_depart = fields.Datetime('Date depart')
    date_arrive = fields.Datetime('Date arrivée')
    ville_depart = fields.Char('Ville depart')
    ville_arrive = fields.Char('Ville arrivée')
    retard = fields.Char('Retard')
