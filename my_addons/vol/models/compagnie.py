from odoo import models, fields

class VolCompagnie(models.Model):
    _name = 'vol.compagnie'
    nom = fields.Char('Nom Compagnie')
    siége_social = fields.Char('Siége Social')
