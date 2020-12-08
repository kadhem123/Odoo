from odoo import models, fields

class Volsiege(models.Model):
    _name = 'vol.siege'
    num_allée = fields.Char('num allée')
    num_rang = fields.Char('numero rang')
    classe = fields.Char('Classe')
