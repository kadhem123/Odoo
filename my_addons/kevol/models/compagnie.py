from odoo import models, fields

class KevolCompagnie(models.Model):
    _name = 'kevol.compagnie'
    nom = fields.Char('Nom Compagnie')
    siege_social = fields.Char('Siége Social')
