from odoo import models, fields

class KevolAvion(models.Model):
    _name = 'kevol.avion'
    type = fields.Char('Type Avion')
    modele = fields.Char('Modele Avion')
    nb = fields.Char('Nombre passagers')
