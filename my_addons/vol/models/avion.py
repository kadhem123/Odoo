from odoo import models, fields

class VolAvion(models.Model):
    _name = 'vol.avion'
    type = fields.Char('Type Avion')
    modele = fields.Char('Modele Avion')
    nb = fields.Char('Nombre passagers')
